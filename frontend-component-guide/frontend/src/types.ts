export interface ComponentName {
  zh: string;
  en: string;
}

export interface ComponentProp {
  name: string;
  type: string;
  default: string;
  description: ComponentName;
  options?: string[];
}

export interface Component {
  id: string;
  name: ComponentName;
  description: ComponentName;
  category: string;
  props: ComponentProp[];
  codeExample: string;
}

export interface Category {
  title: string;
  components: Component[];
}

export interface ApiResponse {
  categories: Record<string, Category>;
  allComponents: Component[];
}