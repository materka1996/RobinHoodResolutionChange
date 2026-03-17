# Zmiana Rozdzielczości w RobinHood Legenda Sherwood

Proste narzędzie z interfejsem graficznym (GUI) do zmiany rozdzielczości ekranu w plikach binarnych profilu gry w wersji 1.1. Skrypt został zaprojektowany z myślą o bezpieczeństwie – automatycznie tworzy kopie zapasowe i pozwala na ich łatwe przywrócenie.

✨ Funkcje
Detekcja aktualnej rozdzielczości: Skrypt skanuje plik i wyświetla aktualnie ustawioną wartość.
Bezpieczeństwo (Backup): Automatycznie tworzy kopię zapasową .bak przed pierwszą modyfikacją.
Przywracanie: Dedykowany przycisk do szybkiego cofnięcia zmian w razie problemów.
Intuicyjne GUI: Czytelny interfejs oparty na bibliotece tkinter.

🚀 Jak zacząć?
Wymagania
Zainstalowany Python 3.x.
Biblioteki standardowe (nie musisz nic doinstalowywać, wszystko jest w pakiecie z Pythonem).

Uruchomienie
Pobierz plik ze skryptem (RobinHoodZmianaRodzielczosciv1.1.py).
Otwórz terminal / wiersz poleceń w folderze ze skryptem.

Uruchom polecenie:

Bash
python RobinHoodZmianaRodzielczosciv1.1.py
📖 Instrukcja użycia
Wybierz plik: Kliknij "Wybierz plik Profiles" i wskaż plik zapisu (zazwyczaj znajduje się w folderze Data/Savegame/Profiles).
Sprawdź status: Skrypt wyświetli wykrytą rozdzielczość (np. Aktualna rozdzielczość: 1920x1080).
Zmień rozdzielczość: Wybierz nową wartość z listy rozwijanej.
Zapisz: Kliknij "Zastosuj zmiany".

Ratunek: Jeśli gra nie uruchamia się poprawnie, użyj przycisku "Przywróć z kopii zapasowej".

🛠️ Obsługiwane rozdzielczości
Skrypt operuje na mapowaniu wartości HEX dla popularnych rozdzielczości:
Standardowe: 640x480 do 1920x1080.
UltraWide / High-Res: 2560x1440, 1600x900 i inne.

⚠️ Uwaga
Modyfikowanie plików binarnych gier odbywa się na własną odpowiedzialność. Zawsze upewnij się, że masz kopię zapasową swoich postępów w grze (skrypt robi ją automatycznie, ale warto mieć też własną!).


ENG:
Dear users, this is my fan program, thanks to which you will change the resolution of your game RobinHood The Legend of Sherwood.
This is version v1.0. If any resolution is missing, let me know, I will update it.

Instructions:
1. Run the file ChangeResolutionRobinHood.exe
2. Search for the location and load the file Profiles Example:
3. [Path]:\Robin Hood - The Legend of Sherwood\DATA\Savegame\Profiles
4. Select the desired resolution and confirm.
