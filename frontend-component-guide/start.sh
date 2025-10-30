#!/bin/bash

echo "启动前端组件中英文对照学习系统..."
echo

# 启动后端服务
echo "正在启动后端服务..."
cd backend
pip install -r requirements.txt
python main.py &
BACKEND_PID=$!
cd ..

# 等待后端启动
sleep 5

# 启动前端服务
echo "正在启动前端服务..."
cd frontend
npm start &
FRONTEND_PID=$!
cd ..

echo
echo "系统启动完成！"
echo "后端API: http://localhost:8000"
echo "前端应用: http://localhost:3000"
echo
echo "按 Ctrl+C 关闭所有服务..."

# 等待用户中断
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait