<script setup>
import { zhCN, dateZhCN, NConfigProvider, NMessageProvider, NDialogProvider, NNotificationProvider, NLoadingBarProvider } from 'naive-ui'
import { reactive, ref } from 'vue';

const locale = ref(null);
const dateLocale = ref(null);


</script>

<template>
  <n-config-provider :locale="zhCN" :date-locale="dateZhCN">
    <n-loading-bar-provider>
      <n-message-provider>
        <n-dialog-provider>
          <n-notification-provider>
            <RouterView></RouterView>
          </n-notification-provider>
        </n-dialog-provider>
      </n-message-provider>
    </n-loading-bar-provider>
  </n-config-provider>
</template>

<style scoped></style>
