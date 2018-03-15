# Certbot (Modified)

## Disclaimer

This is a Hack Version based on the Let's Encrypt offical [certbot](https://github.com/certbot/certbot). Only tested with Python 3.7.

## Usage

```
sudo ~/.local/share/certbot/bin/certbot certonly --dns-google --dns-google-credentials /path/to/your/google-gcloud-dns-credential.json -d '*.example.com' -d example.com
```