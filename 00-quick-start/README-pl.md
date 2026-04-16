# Szybki start (Quick Start)

W tym rozdziale zainstalujesz GitHub Copilot CLI, zalogujesz się na konto GitHub i zweryfikujesz działanie narzędzia. To krótka instrukcja uruchomienia — dalsze demonstracje zaczynają się w Rozdziale 01.

## Cele

- Zainstalować Copilot CLI
- Zalogować się do GitHub
- Sprawdzić działanie na prostym teście

## Wymagania

- Konto GitHub z dostępem do Copilot
- Podstawowa znajomość terminala (cd, ls)

## Instalacja

Możesz użyć Codespaces (brak konfiguracji) lub zainstalować lokalnie:

- npm: `npm install -g @github/copilot`
- Homebrew (macOS/Linux): `brew install copilot-cli`
- WinGet (Windows): `winget install GitHub.Copilot`
- Skrypt instalacyjny: `curl -fsSL https://gh.io/copilot-install | bash`

## Uwierzytelnianie

Uruchom `copilot` w katalogu repozytorium, zaufaj folderowi, a następnie wykonaj `/login` i postępuj zgodnie z instrukcjami urządzenia.

## Weryfikacja

- Otwórz Copilot i zapytaj o pomoc, otrzymasz odpowiedź asystenta
- Uruchom przykładową aplikację: `cd samples/book-app-project && python book_app.py list`

## Rozwiązywanie problemów

- "copilot: command not found" — zainstaluj CLI (patrz powyżej)
- Brak dostępu do Copilot — sprawdź subskrypcję na github.com/settings/copilot

Gotowe — możesz przejść do Rozdziału 01.