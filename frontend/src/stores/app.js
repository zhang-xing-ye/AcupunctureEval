import { defineStore } from 'pinia'
import { ref } from 'vue'
import i18n from '@/locales'

export const useAppStore = defineStore('app', () => {
    // 浏览器默认语言或者默认中文
    const savedLocale = localStorage.getItem('locale')
    const systemLocale = navigator.language === 'zh-CN' ? 'zh-CN' : 'en-US'
    const locale = ref(savedLocale || systemLocale)

    function setLocale(lang) {
        locale.value = lang
        i18n.global.locale.value = lang
        localStorage.setItem('locale', lang)
    }

    // 初始化
    if (i18n.global.locale.value !== locale.value) {
        i18n.global.locale.value = locale.value
    }

    return {
        locale,
        setLocale
    }
})
