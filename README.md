# l10n_csv2mobile
Convert from localization in CSV to iOS (Localizable.strings) and Android (strings.xml) files

# Why you need
You have a single product that need l10n in both iOS and Android. When you have the new update on translations, you need to update to both platforms. Now just a command can help you.

# How to use
* Keep the translations in csv file like the example (translations.csv). It has key, original string and translated strings.
* Remember to update the locale list in file csv2mobile.py to match the locale in translations.csv
* Run `python csv2mobile.py`

# Build integration
You can keep the translation file in the repository and integrate it with the build pipeline someway.
For example:
* iOS
```
cp translations.csv
python csv2mobile.py
cp -R ios/* [ios_project_location]/Supporting\ Files/*
```
* Android
```
cp translations.csv
python csv2mobile.py
cp -R android/* [android_project_location]/res/*
```
