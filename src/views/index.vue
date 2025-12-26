<template>
    <div class="flex flex-col min-h-screen bg-slate-50 font-sans">
        <!-- Top Navigation -->
        <header class="sticky top-0 z-50 w-full">
            <Navbar />
        </header>

        <!-- Main Content Area -->
        <main class="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <router-view v-slot="{ Component }">
                <transition name="fade" mode="out-in">
                    <component :is="Component" />
                </transition>
            </router-view>
        </main>

        <!-- Footer -->
        <footer class="bg-white border-t border-gray-200 py-8 mt-auto">
            <div class="max-w-7xl mx-auto px-4 text-center">
                <p class="text-gray-500 text-sm">
                    &copy; {{ new Date().getFullYear() }} TCM Benchmark. All Rights Reserved.
                </p>
                <p class="text-gray-400 text-xs mt-2">
                    A Comprehensive Benchmark for Traditional Chinese Medicine Large Language Models
                </p>
            </div>
        </footer>
    </div>
</template>

<script setup>
import Navbar from '@/components/Navbar.vue'
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease, transform 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
    transform: translateY(5px);
}
</style>
