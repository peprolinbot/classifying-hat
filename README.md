# The Classifying Hat

<img src="classifyingHat/static/classifyingHat/logo.svg" alt="The Classifying Hat" width=200/>

[![Docker Repository on Quay](https://quay.io/repository/peprolinbot/classifying-hat/status "Docker Repository on Quay")](https://quay.io/repository/peprolinbot/classifying-hat)

Discover to which Hogwart's house you belong with the help of a magical machine learning model, which should provide a more scientifically accurate result than your typical test.

Yeah, the name is a joke, beacause this uses what's known as a 'classifier' model. If you're a muggle (you don't know the magic spells of coding and probably use Windows or MacOS) you could say this is Hacendado's Sorting Hat.

You can find an instance hosted by myself on [clashat.peprolinbot.com](https://clashat.peprolinbot.com).

## 🧠 Train it

Under `utils` you'll find the dataset (`harry_all.csv`), directly downloaded from [osf.io/rtf74](https://osf.io/rtf74/), and the script (`train_model.py`) that trains the ML moel (Gaussian Naive Bayes).

To train the model, just run `train_model.py` from within the directory without any arguments. Once it finishes, you must move `model.pkl` to the root of the project.

## 🔧 How to Install

### 🐳 Docker (Recommended)

If you want to host your own instance of the web, it is as easy as a docker container.

So the command is:
 
```bash
docker run -d --name classifying-hat \
    -e DJANGO_ALLOWED_HOSTS="example.com" \
    -e DJANGO_SECRET_KEY="changemetosomethingsecureplease" \
    -p 8080:80 \
    quay.io/peprolinbot/classifying-hat:latest
```

Or you can also use the `docker-compose.yml` file at the root of this repo. You know: `docker-compose up -d`.

#### Environment Variables

| Name                     | Description |
|--------------------------|-------------|
| `DJANGO_DEBUG` (bool)    | Whether to enable Django's debug mode. Leave it false in production. _(Default: False)_
| `DJANGO_ALLOWED_HOSTS` | Space-separated list of host/domain names that Django can serve. Not needed in debug mode. _(Default: "")_
| `DJANGO_SECRET_KEY`  |  The key to securing signed data. Must be randomly generated and kept secure. _(Default: "django-insecure-(krka)#p79n81tjf-dy9f1!k^4*j&+qf5_eurt7)o%8%mr1ce")_
| `GUNICORN_WORKERS`  |  Gunicorn's `--workers` argument _(Default: 3)_
| `GUNICORN_TIMEOUT`  |  Gunicorn's `--timeout` argument _(Default: 30)_

_**Note🗒️:**_ DJANGO_DEBUG is true only when the variable's value is the string "true" (not case sensitive)

_**Tip💡:**_ You can generate a secret key with `openssl rand -hex 32`

#### Building the image

```bash
git clone https://codeberg.org/peprolinbot/classifying-hat.git
cd classifying-hat
docker build -t classifying-hat .
```

### 💪🏻 Without Docker (for development)

Only use this for development unless you know what you're doing.

```bash
git clone https://codeberg.org/peprolinbot/classifying-hat.git
cd classifying-hat
export DJANGO_DEBUG=true
python3 manage.py runserver
```

Please check [Django's documentation](https://docs.djangoproject.com/en/4.1/).

## ⚠️ Disclaimer

This project is not endorsed by, directly affiliated with, maintained by, sponsored by or in any way officially related with Wizarding World, Warner Bros, J. K. Rowling or any of the companies and individuals involved in the Harry Potter franchise.

## ❤️ Credits
	
- Web background image: By [Alfonso Cerezo](https://pixabay.com/users/alfcermed-3552488) from [Pixabay](https://pixabay.com/photos/dining-room-banquet-oxford-5114247/)

- House logos: From [Harry Potter Wiki](https://harrypotter.fandom.com/) on [Fandom](fandom.com)

- Logo font: [Harry P](https://www.dafont.com/harry-p.font) by [Graham Meade](https://www.dafont.com/profile.php?user=146134)

- Logo hat: by [OpenClipart-Vectors](https://pixabay.com/users/openclipart-vectors-30363/) from [Pixabay](https://pixabay.com/vectors/chapeau-hat-magic-1293080)

- Logo gears: by [OpenClipart-Vectors](https://pixabay.com/users/openclipart-vectors-30363/) from [Pixabay](https://pixabay.com/vectors/cogwheel-gear-gearwheel-cog-145804/)

- This uses the data collected in [_The Science Behind the Magic? The Relation of the Harry Potter “Sorting Hat Quiz” to Personality and Human Values_](https://doi.org/10.1525/collabra.240) by Lea Jakob, Eduardo Garcia-Garzon, Hannes Jarke, and Fabian Dablander. DOI: [doi.org/10.1525/collabra.240](https://doi.org/10.1525/collabra.240)