import sys
from pathlib import Path
from colorama import init, Fore, Style

# Включаем colorama для цветов
init()


def show_folder_structure(path, level=0):
    try:
        items = list(path.iterdir())

        for item in items:
            # ⬇⬇⬇ ВАЖНО: Пропускаем папку .venv ⬇⬇⬇
            if item.name == '.venv' and item.is_dir():
                indent = "    " * level
                if level > 0:
                    indent = "│   " * (level - 1) + "├── "
                print(f"{indent}📁 {Fore.CYAN}{item.name} [пропущено]")
                continue  # НЕ заходим в .venv!
            # ⬆⬆⬆ ВАЖНО: Пропускаем папку .venv ⬆⬆⬆

            # Делаем отступ
            indent = "    " * level
            if level > 0:
                indent = "│   " * (level - 1) + "├── "

            if item.is_dir():
                print(f"{indent}📁 {Fore.BLUE}{item.name}")
                show_folder_structure(item, level + 1)
            else:
                print(f"{indent}📄 {Fore.GREEN}{item.name}")

    except PermissionError:
        indent = "    " * level
        print(f"{indent}{Fore.YELLOW}⚠ Нет доступа")
    except Exception as e:
        indent = "    " * level
        print(f"{indent}{Fore.RED}✗ Ошибка: {e}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Использование: python {Path(__file__).name} <путь к папке>")
        print(f"{Fore.CYAN}Пример: python {Path(__file__).name} .")
        return

    user_path = sys.argv[1]
    path = Path(user_path)

    if not path.exists():
        print(f"{Fore.RED}❌ Ошибка: Папки '{user_path}' нет!")
        return

    if not path.is_dir():
        print(f"{Fore.RED}❌ Ошибка: '{user_path}' это не папка!")
        return

    print(f"\n{Fore.CYAN}{'=' * 50}")
    print(f"{Fore.CYAN}📁 Что в папке: {path}")
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}\n")

    show_folder_structure(path)

    print(f"\n{Fore.CYAN}{'=' * 50}")
    print(f"{Fore.CYAN}✅ Готово!")
    print(f"{Fore.CYAN}{'=' * 50}")


if __name__ == "__main__":
    main()