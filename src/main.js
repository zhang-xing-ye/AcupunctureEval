import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import VueUiXy from "vue-data-ui/vue-ui-xy";

createApp(App).use(createPinia()).use(router).component('VueUiXy', VueUiXy).mount('#app')
