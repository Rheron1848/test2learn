@echo off
echo 启动前端组件中英文对照学习系统...
echo.

REM 启动后端服务
echo 正在启动后端服务...
cd backend
start cmd /k "python -m pip install -r requirements.txt && python main.py"
timeout /t 5 /nobreak > nul

REM 启动前端服务
echo 正在启动前端服务...
cd ../frontend
start cmd /k "npm start"

echo.
echo 系统启动完成！
echo 后端API: http://localhost:8000
echo 前端应用: http://localhost:3000
echo.
echo 按任意键关闭所有服务...
pause > nul

REM 关闭所有Node.js和Python进程
taskkill /F /IM node.exe 2> nul
taskkill /F /IM python.exe 2> nul
exit