# MusicSplit

To run the backend functionality, spleeter and ffmpeg must be set up. ffmpeg must also be added to PATH. Other libraries that are used include pytube and Spotify's basic pitch. Note that pytube can be occasionally broken while maintainers work on patches.

To run the project in development, open two terminals:
```
cd frontend
npm run dev
```

```
cd backend
python manage.py runserver
```