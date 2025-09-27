use eframe::{egui, App};
use std::process::Command;

#[derive(Default)]
struct AppState {
    ask_nickname: bool,
    nickname: String,
}

impl App for AppState {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            if !self.ask_nickname {
                if ui.button("Играть!").clicked() {
                    self.ask_nickname = true;
                }
            } else {
                ui.label("Введите ваш никнейм:");
                ui.text_edit_singleline(&mut self.nickname);

                if ui.button("Продолжить").clicked() {
                    println!("ник игрока : '{}' ", self.nickname);

                    // 🔥 Запускаем pygame скрипт
                    let result = Command::new("python")
                        .arg("main.py") // тут путь до твоего pygame файла
                        .spawn();

                    match result {
                        Ok(_) => println!("pygame запущен!"),
                        Err(e) => eprintln!("Ошибка запуска pygame: {}", e),
                    }

                    // Можно свернуть/закрыть egui после запуска игры
                    self.ask_nickname = false;
                }
            }
        });
    }
}

fn main() -> eframe::Result<()> {
    let options = eframe::NativeOptions::default();
    eframe::run_native(
        "tinkytestversion1-ww",
        options,
        Box::new(|_cc| Ok(Box::new(AppState::default()))),
    )
}
