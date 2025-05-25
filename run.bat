@echo off

start "Running API" cmd /k "cd api && python -m run"

start "Running UI" cmd /k "cd ui && npm run dev"