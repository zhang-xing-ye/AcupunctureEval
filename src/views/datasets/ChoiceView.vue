<template>
    <DatasetSection :sections="sections" />
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import DatasetSection from './components/DatasetSection.vue'

const { t } = useI18n()

// Common columns for choice questions
const commonColumns = [
    { title: () => t('datasets.columns.id'), key: 'id', width: 80 },
    { title: () => t('datasets.columns.question'), key: 'question', ellipsis: { tooltip: true } },
    { title: () => t('datasets.columns.option_a'), key: 'A', width: 150 },
    { title: () => t('datasets.columns.option_b'), key: 'B', width: 150 },
    { title: () => t('datasets.columns.option_c'), key: 'C', width: 150 },
    { title: () => t('datasets.columns.option_d'), key: 'D', width: 150 },
    { title: () => t('datasets.columns.option_e'), key: 'E', width: 150 },
    { title: () => t('datasets.columns.answer'), key: 'answer', width: 80, align: 'center' }
]

// Data Mocks (Keep text content as is)
const a1Data = [
    { id: 1, question: "下列各项，不属天麻和全蝎主治病证的是", A: "小儿急慢惊风", B: "脾虚慢惊", C: "破伤风证", D: "风湿痹证", E: "风中经络", answer: "B" },
    { id: 2, question: "治疗肝火犯胃，呕吐吞酸，黄连常配伍的药物是", A: "丁香", B: "干姜", C: "花椒", D: "小茴香", E: "吴茱萸", answer: "E" },
    { id: 3, question: "下列各项，不属镇心安神药组的是", A: "龙骨、牡蛎", B: "朱砂、磁石", C: "龟甲、鳖甲", D: "珍珠、琥珀", E: "珍珠母、紫贝齿", answer: "C" },
    { id: 4, question: "患者，女，30岁。心悸，气促2个月，咯粉红色泡沫痰。检查：面颊暗红，口唇发绀，听诊二尖瓣面容，心尖区可闻及舒张期隆隆样杂音，触诊有震颤。其诊断是", A: "肺源性心脏病", B: "冠心病", C: "二尖瓣狭窄", D: "主动脉瓣狭窄", E: "心包积液", answer: "C" },
    { id: 5, question: "患者，女，50岁。家属代诉：刚才与人争吵，突然昏倒，不省人事。见面色苍白，汗出，四肢冷，心率50次／分，血压90／60mmHg。左上腹压痛，肠鸣音亢进。血红蛋白60g／L。应首先考虑的是", A: "心源性休克", B: "感染性休克", C: "失血性休克", D: "过敏性休克", E: "神经源性休克", answer: "C" }
]

const a2Data = [
    { id: 1, question: "患儿，2岁。发热2天，鼻塞流涕，咳嗽剧烈，呼吸气促，喉间痰鸣，双肺闻及哮鸣音。其诊断是", A: "感冒夹惊", B: "感冒夹痰", C: "肺炎喘嗽", D: "哮喘", E: "顿咳", answer: "D" },
    { id: 2, question: "患者，男，50岁。半年来经常突发胸骨后疼痛，有窒息感，持续约1～5分钟，休息后迅速缓解。心电图示ST段下移及T波倒置。应首先考虑的是", A: "心绞痛", B: "急性心肌梗死", C: "心包炎", D: "心肌炎", E: "肋间神经痛", answer: "A" },
    { id: 3, question: "患者，女，26岁。产后20天，乳房胀痛，乳漏不止，要求回乳。宜选用的药物是", A: "炒麦芽", B: "炒谷芽", C: "炒神曲", D: "炒山楂", E: "炒槟榔", answer: "A" },
    { id: 4, question: "患者，男，30岁。高热寒战2天，胸痛，伴咳嗽，痰中带血。听诊：右肺中部可闻及湿啰音。应首先考虑的是", A: "急性支气管炎", B: "肺炎", C: "肺结核", D: "肺癌", E: "支气管哮喘", answer: "B" },
    { id: 5, question: "患者，女，45岁。失眠2个月，近日来入睡困难，心烦，手足心热，盗汗，口干少津，舌红少苔，脉细数。治疗应首选", A: "安神定志丸", B: "黄连阿胶汤", C: "琥珀多寐丸", D: "镇肝熄风汤", E: "酸枣仁汤", answer: "E" }
]

const a3Data = [
    { id: 1, question: "（1-3题共用题干）\n患者，男，60岁。慢性支气管炎病史20年，肺心病病史5年。近1周感冒后咳嗽，咳痰，气促加重，伴尿少，下肢水肿，腹胀，纳差。查体：呼吸急促，口唇发绀，双肺底闻及湿啰音，心率110次／分，律齐，肝肋下3cm，有压痛，下肢水肿(++)。\n1. 该患者目前的治疗原则是", A: "控制感染", B: "改善通气", C: "纠正缺氧", D: "控制心力衰竭", E: "以上都是", answer: "E" },
    { id: 2, question: "2. 经治疗后，患者病情好转，水肿消退，但出现手足搐搦。应考虑的并发症是", A: "呼吸性酸中毒", B: "呼吸性碱中毒", C: "代谢性酸中毒", D: "代谢性碱中毒", E: "低钙血症", answer: "D" },
    { id: 3, question: "3. 针对上述并发症，应采取的治疗措施是", A: "补酸", B: "补碱", C: "补氯化钾", D: "补钙", E: "补镁", answer: "C" },
    { id: 4, question: "（4-5题共用题干）\n患者，女，35岁。月经周期正常，经期延长，经量多，色红，质稠，伴小腹疼痛，口干，便秘，舌红，苔黄，脉数。\n4. 其证候是", A: "气虚证", B: "血热证", C: "血瘀证", D: "湿热证", E: "阴虚证", answer: "B" },
    { id: 5, question: "5. 治疗应首选的方剂是", A: "保阴煎", B: "固经丸", C: "清经散", D: "举元煎", E: "两地汤", answer: "A" }
]

const sections = ref([
    {
        title: () => t('datasets.choice.a1.title'),
        description: () => t('datasets.choice.a1.desc'),
        githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A1.json',
        columns: commonColumns,
        data: a1Data,
        codeExample: `
{
  "exam_type": "A1",
  "question": "下列各项，不属天麻和全蝎主治病证的是",
  "option": {
    "A": "小儿急慢惊风",
    "B": "脾虚慢惊",
    "C": "破伤风证",
    "D": "风湿痹证",
    "E": "风中经络"
  },
  "answer": "B"
}`
    },
    {
        title: () => t('datasets.choice.a2.title'),
        description: () => t('datasets.choice.a2.desc'),
        githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A2.json',
        columns: commonColumns,
        data: a2Data,
        codeExample: `
{
  "exam_type": "A2",
  "question": "患儿，2岁。发热2天，鼻塞流涕，咳嗽剧烈，呼吸气促，喉间痰鸣，双肺闻及哮鸣音。其诊断是",
  "option": {
    "A": "感冒夹惊",
    "B": "感冒夹痰",
    "C": "肺炎喘嗽",
    "D": "哮喘",
    "E": "顿咳"
  },
  "answer": "D"
}`
    },
    {
        title: () => t('datasets.choice.a3.title'),
        description: () => t('datasets.choice.a3.desc'),
        githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A3.json',
        columns: commonColumns,
        data: a3Data,
        codeExample: `
{
  "exam_type": "A3",
  "question": "（1-3题共用题干）\\n患者，男，60岁。慢性支气管炎病史20年，肺心病病史5年。近1周感冒后咳嗽，咳痰，气促加重，伴尿少，下肢水肿，腹胀，纳差。查体：呼吸急促，口唇发绀，双肺底闻及湿啰音，心率110次／分，律齐，肝肋下3cm，有压痛，下肢水肿(++)。\\n1. 该患者目前的治疗原则是",
  "option": {
    "A": "控制感染",
    "B": "改善通气",
    "C": "纠正缺氧",
    "D": "控制心力衰竭",
    "E": "以上都是"
  },
  "answer": "E"
}`
    },
    {
        title: () => t('datasets.choice.a4.title'),
        description: () => t('datasets.choice.a4.desc'),
        githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A4.json',
        columns: commonColumns,
        data: [], // Placeholder
        codeExample: `
{
  "exam_type": "A4",
  "question": "...",
  "option": { ... },
  "answer": "A"
}`
    },
    {
        title: () => t('datasets.choice.b.title'),
        description: () => t('datasets.choice.b.desc'),
        githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/B.json',
        columns: commonColumns,
        data: [], // Placeholder
        codeExample: `
{
  "exam_type": "B",
  "question": "...",
  "option": { ... },
  "answer": "C"
}`
    },
    {
        title: () => t('datasets.choice.x.title'),
        description: () => t('datasets.choice.x.desc'),
        githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/X.json',
        columns: commonColumns,
        data: [], // Placeholder
        codeExample: `
{
  "exam_type": "X",
  "question": "...",
  "option": { ... },
  "answer": "ABC"
}`
    }
])
</script>
