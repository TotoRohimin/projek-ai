from googletrans import Translator
from termcolor import colored
from pyfiglet import Figlet

class SistemPenerjemah:
    def __init__(self):
        self.translator = Translator()
        self.figlet = Figlet(font='slant')

    def translate_text(self, text, target_language='en'):
        translation = self.translator.translate(text, dest=target_language)
        return translation.text

    def print_header(self):
        header = self.figlet.renderText('SITPENTO')
        print(colored(header, 'cyan'))
        print(colored("🚀 Selamat datang di Sistem Penerjemah Toto (SITPENTO)! 🌈", 'green'))
        print(colored("=" * 50, 'cyan'))

    def get_user_input(self):
        source_text = input(colored("📝 Masukkan teks yang ingin diterjemahkan: ", 'yellow'))
        target_language = input(colored("🌍 Masukkan kode bahasa tujuan (contoh: 'en' untuk bahasa Inggris): ", 'yellow'))
        return source_text, target_language

    def display_translation(self, source_text, target_language, translated_text):
        print(f"\n📝 Teks asli (ID): {colored(source_text, 'yellow')}")
        print(f"\n🌍 Terjemahan ke {colored(target_language.upper(), 'yellow')}: {colored(translated_text, 'green')}")

    def print_footer(self):
        print(colored("=" * 50, 'cyan'))
        print(colored("🌐 Ditenagai oleh Google Translate API", 'cyan'))
        print(colored("💡 Tip: Gunakan kode bahasa ISO untuk hasil terbaik", 'cyan'))
        print(colored("=" * 50, 'cyan'))

    def print_goodbye(self):
        print(colored("🚀 Program selesai. Terima kasih telah menggunakan Sistem Penerjemah Toto (SITPENTO)!", 'green'))
        print(colored("=" * 50, 'cyan'))

    def run(self):
        self.print_header()

        # Meminta input dari pengguna
        source_text, target_language = self.get_user_input()

        # Menerjemahkan teks
        translated_text = self.translate_text(source_text, target_language)

        # Menampilkan hasil terjemahan
        self.display_translation(source_text, target_language, translated_text)

        self.print_footer()
        self.print_goodbye()

if __name__ == "__main__":
    translator_app = SistemPenerjemah()
    translator_app.run()
