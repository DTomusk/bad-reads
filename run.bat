@echo off

start "" cmd /k "cd api && python -m run"

start "" cmd /k "cd ui && npm run dev"