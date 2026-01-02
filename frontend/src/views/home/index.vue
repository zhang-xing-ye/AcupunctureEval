<template>
    <div class="space-y-16 pb-12">
        <!-- 1. 统计区域 -->
        <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <div v-for="(stat, index) in stats" :key="index"
                class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-300 flex items-center gap-4 group">
                <div
                    class="w-12 h-12 rounded-lg bg-teal-50 text-teal-600 flex items-center justify-center group-hover:bg-teal-600 group-hover:text-white transition-colors duration-300">
                    <component :is="stat.icon" class="w-6 h-6" />
                </div>
                <div>
                    <div class="text-sm text-gray-500 font-medium uppercase tracking-wider">{{ t(stat.labelKey) }}</div>
                    <div class="text-2xl font-bold text-gray-900 mt-1">
                        <n-number-animation :from="0" :to="stat.value" :duration="2000" />
                        <span v-if="stat.suffix" class="text-sm font-normal text-gray-400 ml-1">{{ stat.suffix }}</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. 介绍区域 -->
        <section class="text-center max-w-4xl mx-auto space-y-6">
            <h2 class="text-3xl font-bold text-gray-900 font-serif">{{ t('home.intro.title') }}</h2>
            <div class="w-20 h-1 bg-teal-600 mx-auto rounded-full"></div>
            <p class="text-lg text-gray-600 leading-relaxed text-justify md:text-center">
                {{ t('home.intro.content') }}
            </p>
        </section>

        <!-- 3. 图片区域 -->
        <section class="select-none relative group/carousel">
            <n-carousel autoplay draggable :interval="3000" :slides-per-view="slidesPerView" :space-between="32"
                effect="slide" class="pb-12" dot-type="line">
                <div v-for="(img, index) in images" :key="index" class="h-full">
                    <div class="space-y-4 group h-full px-1">
                        <div
                            class="aspect-[4/3] rounded-lg overflow-hidden shadow-md border border-gray-200 relative bg-gray-50">
                            <div class="absolute inset-0 bg-gray-100 animate-pulse z-10" v-if="!img.loaded"></div>
                            <n-image :src="img.src" :alt="t(img.titleKey)" object-fit="cover"
                                class="w-full h-full flex justify-center items-center"
                                :img-props="{ class: 'w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-500 cursor-zoom-in' }"
                                :intersection-observer-options="{ rootMargin: '50px' }" lazy
                                @load="img.loaded = true" />
                        </div>
                        <div class="text-center px-2">
                            <h3
                                class="text-lg font-bold text-gray-900 mb-2 group-hover:text-teal-600 transition-colors">
                                {{ t(img.titleKey) }}
                            </h3>
                            <p class="text-sm text-gray-500 leading-relaxed">{{ t(img.descKey) }}</p>
                        </div>
                    </div>
                </div>


                <!-- 自定义指示点样式 -->
                <template #dots="{ total, currentIndex, to }">
                    <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 flex space-x-2">
                        <div v-for="index in total" :key="index"
                            :class="['h-1.5 rounded-full transition-all duration-300 cursor-pointer', currentIndex === index - 1 ? 'w-8 bg-teal-600' : 'w-2 bg-gray-300 hover:bg-gray-400']"
                            @click="to(index - 1)">
                        </div>
                    </div>
                </template>
            </n-carousel>
        </section>

        <!-- 4. 图表区域 -->
        <section class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- 图表1：环形图 -->
            <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                <h3 class="text-xl font-bold text-gray-900 mb-6 border-l-4 border-teal-600 pl-4 relative z-10">{{
                    t('home.charts.chart1_title') }}</h3>
                <div class="w-full h-[500px] flex items-center justify-center">
                    <VueUiDonut :dataset="datasetDistribution" :config="donutConfig" />
                </div>
            </div>

            <!-- 图表2：柱状图（XY） -->
            <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                <h3 class="text-xl font-bold text-gray-900 mb-6 border-l-4 border-teal-600 pl-4 relative z-10">{{
                    t('home.charts.chart2_title') }}</h3>
                <div class="w-full h-[500px] flex items-center justify-center">
                    <VueUiXy :dataset="subjectDistribution" :config="xyConfig" />
                </div>
            </div>
        </section>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { FileText, MessageCircle, Video } from 'lucide-vue-next'

const { t } = useI18n()

// 响应式轮播图显示数量
const slidesPerView = ref(3)
const updateSlidesPerView = () => {
    const width = window.innerWidth
    if (width < 640) {
        slidesPerView.value = 1
    } else if (width < 1024) {
        slidesPerView.value = 2
    } else {
        slidesPerView.value = 3
    }
}

onMounted(() => {
    updateSlidesPerView()
    window.addEventListener('resize', updateSlidesPerView)
})

onUnmounted(() => {
    window.removeEventListener('resize', updateSlidesPerView)
})

// 1. 统计数据
const stats = ref([
    {
        labelKey: 'home.stats.qa_count',
        value: 47797,
        // suffix: '+',
        icon: FileText
    },
    {
        labelKey: 'home.stats.vqa_count',
        value: 10729,
        // suffix: '+',
        icon: MessageCircle
    },
    {
        labelKey: 'home.stats.video_count',
        value: 1000,
        suffix: '+',
        icon: Video
    }
])

// 3. 图片数据
const images = ref([
    {
        src: '/val_test.png',
        titleKey: 'home.images.val_test_title',
        descKey: 'home.images.val_test_desc',
        loaded: false
    },
    {
        src: '/dataset_classify.png',
        titleKey: 'home.images.dataset_classify_title',
        descKey: 'home.images.dataset_classify_desc',
        loaded: false
    },
    {
        src: '/TCM_symptom_semantic_clusters_irregular.jpg',
        titleKey: 'home.images.tcm_symptom_title',
        descKey: 'home.images.tcm_symptom_desc',
        loaded: false
    },
    {
        src: '/vqa_classify.png',
        titleKey: 'home.images.vqa_classify_title',
        descKey: 'home.images.vqa_classify_desc',
        loaded: false
    },
    {
        src: '/xuewei_classify.png',
        titleKey: 'home.images.xuewei_classify_title',
        descKey: 'home.images.xuewei_classify_desc',
        loaded: false
    },
    {
        src: '/Figure_Strict_Acupoint_Clusters.jpg',
        titleKey: 'home.images.figure_strice_title',
        descKey: 'home.images.figure_strice_desc',
        loaded: false
    },
    {
        src: '/pig_xuewei.png',
        titleKey: 'home.images.pig_xuewei_title',
        descKey: 'home.images.pig_xuewei_desc',
        loaded: false
    }

])

// 4. 图表数据与配置
// 环形图数据（数据集分布）
const datasetDistribution = ref([
    { name: 'QA Object', values: [1735], color: '#0d9488' },
    { name: 'QA Subject', values: [46062], color: '#14b8a6' },
    { name: 'VQA', values: [10729], color: '#5eead4' },
    { name: 'Video', values: [1000], color: '#ccfbf1' }
])

const donutConfig = ref({
    style: {
        chart: {
            backgroundColor: "#FFFFFF",
            color: "#1f2937",
            layout: {
                labels: {
                    dataLabels: {
                        show: true,
                        useLabelSlots: false,
                        hideUnderValue: 3
                    }
                }
            },
            legend: {
                backgroundColor: "#FFFFFF",
                color: "#1f2937",
                show: true
            },
            title: {
                text: "",
                color: "#1f2937",
            }
        }
    }
})

// XY图数据（学科分布）
const subjectDistribution = ref([
    {
        name: 'Questions',
        series: [2500, 1800, 3200, 1500, 2200],
        type: 'bar',
        color: '#0d9488'
    }
])

const xyConfig = ref({
    chart: {
        labels: {
            xAxisLabels: {
                values: ['Internal Med', 'Surgery', 'Acupuncture', 'Diagnosis', 'Prescriptions'],
                color: "#1f2937"
            }
        },
        grid: {
            stroke: "#e5e7eb"
        },
        userOptions: {
            show: false
        }
    },
    style: {
        chart: {
            backgroundColor: "#FFFFFF",
            color: "#1f2937",
            title: {
                text: "",
                color: "#1f2937"
            }
        }
    },
    bar: {
        borderRadius: 4,
        useGradient: false
    }
})

</script>
