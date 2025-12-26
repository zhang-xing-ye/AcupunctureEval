<script setup>
import { zhCN, dateZhCN } from 'naive-ui'
import { reactive, ref } from 'vue';
const locale = ref(null);
const dateLocale = ref(null);


</script>

<template>
  <n-config-provider :locale="zhCN" :date-locale="dateZhCN">
    <RouterView></RouterView>
  </n-config-provider>
</template>

<style scoped></style>
