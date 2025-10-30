import axios from 'axios';
import { ApiResponse, Component } from '../types';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
});

export const componentApi = {
  getAllComponents: async (): Promise<ApiResponse> => {
    const response = await api.get('/components');
    return response.data;
  },

  getComponent: async (id: string): Promise<Component> => {
    const response = await api.get(`/components/${id}`);
    return response.data;
  },

  getCategories: async (): Promise<string[]> => {
    const response = await api.get('/categories');
    return response.data;
  },
};