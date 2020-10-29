# Mikroserwis RestAPI do wysyłania emaila

autor: Tomasz Wiśniewski

**Instrukcja instalacji:**

1. Sklonuj repozytorium za pomocą polecenia: `$git clone https://github.com/Wisnia44/sendemail.git`;
2. Przejdź do katalogu sendemail: `$cd sendemail`;
3. Poproś autora o klucz konfiguracji usługi sparkpost i wklej go w linii `10` pliku `server.py`;
4. Zbuduj obraz dockera: `$docker build -t sendemail .`;
5. Uruchom kontener: `$docker-compose up`;
6. Serwer jest uruchomiony!


**Instrukcja użycia:**

Pod adres `http://0.0.0.0:33302/sendemail` wysyłamy zapytanie metodą POST o części body w formacie json o zadanej strukturze:

```
{
	"recipient": "<adres email adresata>",
	"subject": "<tytuł wiadomości>",
	"body": "<treść wiadomości>"
}
```

Aby przetestować działanie wyślij maila do samego siebie.

Zwróć uwagę, że email mógł znaleźć się w SPAMie!
