import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Layout',
            component: () => import('@/views/index.vue'),
            redirect: '/home',
            children: [
                {
                    path: 'home',
                    name: 'Home',
                    component: () => import('@/views/home/index.vue')
                },
                {
                    path: 'datasets/choice',
                    name: 'DatasetChoice',
                    component: () => import('@/views/datasets/index.vue'),
                    meta: { type: 'choice' }
                },
                {
                    path: 'datasets/qa',
                    name: 'DatasetQA',
                    component: () => import('@/views/datasets/index.vue'),
                    meta: { type: 'qa' }
                },
                {
                    path: 'datasets/vqa',
                    name: 'DatasetVQA',
                    component: () => import('@/views/datasets/index.vue'),
                    meta: { type: 'vqa' }
                },
                {
                    path: 'datasets/video',
                    name: 'DatasetVideo',
                    component: () => import('@/views/datasets/index.vue'),
                    meta: { type: 'video' }
                },
                {
                    path: 'leaderboard',
                    name: 'Leaderboard',
                    component: () => import('@/views/leaderboard/index.vue')
                }
            ]
        }
    ]
})

export default router
