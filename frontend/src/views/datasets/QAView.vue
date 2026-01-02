<template>
  <DatasetSection :sections="sections" />
</template>

<script setup>
import { ref, h } from 'vue'
import { useI18n } from 'vue-i18n'
import DatasetSection from './components/DatasetSection.vue'

const { t } = useI18n()

// QA Columns
const qaColumns = [
  { title: () => t('datasets.columns.id'), key: 'id', width: 80 },
  { title: () => t('datasets.columns.question'), key: 'question', ellipsis: { tooltip: true } },
  { title: () => t('datasets.columns.answer'), key: 'answer', ellipsis: { tooltip: true } }
]

// Choice Columns
const choiceColumns = [
  { title: () => t('datasets.columns.id'), key: 'id', width: 80, render: (row) => row.id || row.ID },
  { title: () => t('datasets.columns.question'), key: 'question', ellipsis: { tooltip: true } },
  { title: () => t('datasets.columns.option_a'), key: 'A', width: 150, render: (row) => row.A || (row.options && row.options[0]) },
  { title: () => t('datasets.columns.option_b'), key: 'B', width: 150, render: (row) => row.B || (row.options && row.options[1]) },
  { title: () => t('datasets.columns.option_c'), key: 'C', width: 150, render: (row) => row.C || (row.options && row.options[2]) },
  { title: () => t('datasets.columns.option_d'), key: 'D', width: 150, render: (row) => row.D || (row.options && row.options[3]) },
  { title: () => t('datasets.columns.option_e'), key: 'E', width: 150, render: (row) => row.E || (row.options && row.options[4]) },
  // { title: () => t('datasets.columns.answer'), key: 'answer', width: 80, align: 'center' }
]

// MRA Columns
const mraColumns = [
  { title: () => t('datasets.columns.id'), key: 'id', width: 80, render: (row) => row.id || row.ID },
  { title: () => t('datasets.columns.question'), key: 'question', ellipsis: { tooltip: true }, width: 300 },
  { title: () => t('datasets.columns.diagnose'), key: 'diagnose', width: 120 },
  { title: () => t('datasets.columns.syndromes'), key: 'syndromes', width: 120 },
  { title: () => t('datasets.columns.therapy'), key: 'therapy', ellipsis: { tooltip: true } },
  { title: () => t('datasets.columns.prescription'), key: 'prescription', ellipsis: { tooltip: true } },
  { title: () => t('datasets.columns.prescription_meaning'), key: 'meaning of prescriptions', ellipsis: { tooltip: true } },
  { title: () => t('datasets.columns.operation'), key: 'operation', ellipsis: { tooltip: true } }
]

const renderA3A4Expand = (row) => {
  return h('div', { class: 'p-4 bg-gray-50 rounded' }, [
    h('h4', { class: 'font-bold mb-3 text-gray-700' }, t('datasets.columns.question')),
    h('div', { class: 'space-y-4' },
      (row.questions || []).map((q, idx) => {
        return h('div', { class: 'bg-white p-3 rounded border border-gray-200' }, [
          h('div', { class: 'font-medium mb-2' }, `${idx + 1}. ${q.question}`),
          h('div', { class: 'grid grid-cols-1 sm:grid-cols-2 gap-2 pl-2' },
            (q.options || []).map(opt => h('div', { class: 'text-sm text-gray-600' }, opt))
          )
        ])
      })
    )
  ])
}

// A3/A4 Columns
const a3a4Columns = [
  { type: 'expand', key: 'expand', renderExpand: renderA3A4Expand },
  { title: () => t('datasets.columns.id'), key: 'id', width: 80, render: (row) => row.id || row.ID },
  { title: () => t('datasets.columns.shared_query'), key: 'Shared Query', ellipsis: { tooltip: true } }
]

const renderBExpand = (row) => {
  return h('div', { class: 'p-4 bg-gray-50 rounded' }, [
    h('h4', { class: 'font-bold mb-3 text-gray-700' }, t('datasets.columns.question')),
    h('ul', { class: 'list-disc list-inside space-y-1 bg-white p-3 rounded border border-gray-200' },
      (row.questions || []).map((q) => h('li', { class: 'text-gray-700 p-2' }, q.question))
    )
  ])
}

// B Columns
const bColumns = [
  { type: 'expand', key: 'expand', renderExpand: renderBExpand },
  { title: () => t('datasets.columns.id'), key: 'id', width: 80, render: (row) => row.id || row.ID },
  {
    title: () => t('datasets.columns.shared_option'),
    key: 'Shared Option',
    render: (row) => (row['Shared Option'] || []).join('  ')
  }
]

const tcmData = [
  { id: 1, question: "什么是虚呕？", answer: "虚呕是指脾胃虚弱，胃失和降，胃气上逆所致的呕吐。发病缓慢，病程较长。《景岳全书·杂证谟》：凡胃虚作呕者，其证不一，当知所辨。若胃脘不胀者，非实邪也；胸膈不痛者，非气逆也；内无热燥者，非火证也；外无寒热者，非表邪也。无食无火而忽为呕吐者，胃虚也；呕吐无常而时作时止者，胃虚也；食无所停而闻食则呕者，胃虚也；气无所逆而闻气则呕者，胃虚也；或身背、或食饮微寒即呕者，胃虚也；或吞酸，或嗳腐，时苦恶心，兀兀然、泛泛然冷咽靡宁者，胃虚也；或因病误治，妄用克伐寒凉，本无呕而致呕者，胃虚也；或朝食暮吐，暮食朝吐，食人中焦而不化者，胃虚也；食入下焦而不化者，土母无阳，命门虚也。治宜温补。" },
  { id: 2, question: "劳瘿是什么，由什么引起，出自哪本书，孙思邈如何分类和治疗？", answer: "劳瘿为病证名，指瘿病由情绪刺激引起者，出《备急千金要方》卷二十四。孙思邈将瘿分为石瘿、气瘿、劳瘿、土瘿与忧瘿五种，并处五瘿丸以治疗之，即“取鹿靥以佳酒浸令没，炙干，纳酒中更炙，令香，含咽汁，味尽更易，尽十具愈。”" }
]
const acuData = [
  {
    "question": "足少阳络脉的起点和路径是怎样的？",
    "answer": "足少阳络脉的起点和路径为：脉自外踝上5寸处的光明穴分出，走向足厥阴经脉以沟通表里两经，再向下络于足背，这一详细描述来自注解中参见足少阳络脉的部分。",
    "id": 1
  },
  {
    "question": "临床上如何根据手术部位选取手针麻醉的刺激点？",
    "answer": "临床上根据手术部位选取相应刺激点，并辅以体针穴位，如头颈部手术取咽喉点、颈项点透咳喘点、合谷等。",
    "id": 2
  },
]
const mraData = [
  {
    "ID": "试卷1_病案分析题_1",
    "type": "病案分析题",
    "question": "王某，女，32岁，已婚。2019年7月13日初诊。患者近半年来月经先停闭2个月后突然经行量多如注，时而量少淋漓，交替出现，无经净之时，虽经西药止血治疗，未见好转。刻诊：月经量多势急，色红质稠，口渴心烦，尿赤便结，舌红、苔黄，脉数。",
    "diagnose": "崩漏",
    "syndromes": "血热内扰证",
    "therapy": "调理冲任，固崩止漏",
    "prescription": "关元、三阴交、隐白",
    "meaning of prescriptions": "关元为任脉经穴，又与足三阴经交会，有通调冲任、固摄经血的作用；三阴交为足三阴经交会穴，可疏调足三阴之经气，以健脾益胃、调肝固肾、理气调血；隐白为足太阴经井穴，可健脾统血",
    "operation": "关元针尖向下斜刺，使针感传至耻骨联合上下；隐白穴用灯火灸或麦粒灸；气滞血瘀可配合刺络法；肾虚、脾虚可在腹部和背部施灸",
    "id": 1
  },
  {
    "ID": "试卷1_病案分析题_2",
    "type": "病案分析题",
    "question": "张某，女，65岁。2019年12月4日初诊。患者素有高血压史，凌晨5时起床小便，突然出现昏倒，不省人事而送人院。急查：患者神志昏蒙，面赤气粗，喉中痰鸣，两手紧握，牙关紧闭，二便不通，脉弦滑而数。",
    "diagnose": "中风",
    "syndromes": "中脏腑之闭证",
    "therapy": "醒脑开窍，启闭固脱",
    "prescription": "水沟、百会、内关",
    "meaning of prescriptions": "脑为元神之府，督脉入络脑，水沟、百会为督脉穴，可醒脑开窍；内关为心包经络穴，可调理心神、疏通气血",
    "operation": "内关用泻法。水沟用强刺激，以眼球湿润为度。十二井穴用三棱针点刺出血。关元、气海用大艾炷灸，神阙用隔盐灸，不计壮数，以汗止、脉起、肢温为度",
    "id": 2
  },
]

const a1Data = [
  {
    "ID": "1",
    "question": "最早且体系比较完整的针灸专书是（ ）",
    "options": [
      "A.《针灸甲乙经》",
      "B.《灵枢》",
      "C.《明堂孔穴针灸治要》",
      "D.《针灸资生经》",
      "E.《十四经发挥》"
    ]
  },
  {
    "ID": "2",
    "question": "最原始的针刺用具是（ ）",
    "options": [
      "A.骨针",
      "B.竹针",
      "C.砭石",
      "D.陶针",
      "E.铜针"
    ]
  },
]

const a2Data = [
  {
    "ID": "1",
    "question": "不属于中风闭证的症状是（ ）",
    "options": [
      "A. 神志昏迷",
      "B. 面赤气粗",
      "C. 牙关紧闭",
      "D. 二便不通",
      "E. 目合口张"
    ]
  },
  {
    "ID": "2",
    "question": "下列不属于腹痛分型的是（ ）",
    "options": [
      "A. 寒邪内积型",
      "B. 湿热壅滞型",
      "C. 气滞血瘀型",
      "D. 脾胃虚寒型",
      "E. 脾阳不振型"
    ]
  },
]

const a3Data = [
  {
    "ID": "A3_1",
    "Shared Query": "患者，男，38岁，体型偏胖。自诉头晕眼花，视物旋转不定，伴有恶心欲呕，头蒙如裹，神疲困倦，舌胖大，苔白腻，脉濡滑。",
    "questions": [
      {
        "ID": 1,
        "question": "上述病案属于“眩晕”中的（ ）",
        "options": [
          "A. 肝阳上亢证",
          "B. 痰湿中阻证",
          "C. 气血不足证",
          "D. 肾精亏虚证",
          "E. 肝肾阴虚证"
        ]
      },
      {
        "ID": 2,
        "question": "该患者治疗除主穴外，还应根据辨证加用的腧穴是（ ）",
        "options": [
          "A. 行间、侠溪、太溪",
          "B. 丰隆、中脘、阴陵泉",
          "C. 气海、脾俞、胃俞",
          "D. 志室、悬钟、三阴交",
          "E. 肝俞、肾俞、三阴交"
        ]
      }
    ]
  },
]
const a4Data = [
  {
    "ID": "A4_1",
    "Shared Query": "患者，女，60岁。5天前自觉左侧腰胁部皮肤灼热疼痛不适，3天前痛处皮肤出现簇集性粟粒大小的丘状疱疹，呈带状排列，现症见皮损颜色淡红，泡壁松弛，有糜烂渗出液及黄白相间的水疱，脘腹痞闷，苔黄腻，脉滑数。",
    "questions": [
      {
        "question": "针灸治疗本病的治疗原则（ ）",
        "options": [
          "A. 泻火解毒，通络止痛",
          "B. 清热燥湿，通络止痛",
          "C. 祛风止痒，养血和营",
          "D. 清泻肺胃，活血散结",
          "E. 清热润燥，疏风止痒"
        ]
      },
      {
        "question": "该患者辨证分型属于（ ）",
        "options": [
          "A. 肝经火毒",
          "B. 脾经湿热",
          "C. 瘀血阻络",
          "D. 肝脾不调",
          "E. 痰湿阻滞"
        ]
      },
      {
        "question": "该患者治疗除主穴外，还应根据辨证加用的腧穴是（ ）",
        "options": [
          "A. 支沟，阳陵泉",
          "B. 夹脊穴、行间",
          "C. 阴陵泉、血海"
        ]
      }
    ]
  },
]
const bData = [
  {
    "ID": "B_1",
    "Shared Option": [
      "A. 太渊",
      "B. 中府",
      "C. 神门",
      "D. 心俞",
      "E. 内关"
    ],
    "questions": [
      {
        "question": "手太阴之“本”相应腧穴是（ ）"
      },
      {
        "question": "手少阴之“本”相应腧穴是（ ）"
      }
    ]
  },
]
const xData = [
  {
    "ID": "1",
    "question": "下列属俞募配穴法的有（ ）",
    "options": [
      "A. 脾俞、期门",
      "B. 大肠俞、关元",
      "C. 厥阴俞、中脘",
      "D. 肾俞、京门",
      "E. 胆俞、日月"
    ]
  },
  {
    "ID": "2",
    "question": "下列属于足三里主治的有（ ）",
    "options": [
      "A. 胃痛",
      "B. 月经不调",
      "C. 乳痈",
      "D. 癫狂",
      "E. 虚劳"
    ]
  },
]
const sections = ref([
  // QA Sections
  {
    title: () => t('datasets.qa.tcm.title'),
    description: () => t('datasets.qa.tcm.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Clin/CMB-Clin.json',
    columns: qaColumns,
    data: tcmData,
    codeExample: JSON.stringify(tcmData[0], null, 2) // 将中医问答数据的第一条记录格式化为 JSON 字符串，用于代码示例展示
    //       `
    //   {
    //     "question": "什么是虚呕？",
    //     "answer": "虚呕是指脾胃虚弱，胃失和降，胃气上逆所致的呕吐。发病缓慢，病程较长。《景岳全书·杂证谟》：凡胃虚作呕者，其证不一，当知所辨。若胃脘不胀者，非实邪也；胸膈不痛者，非气逆也；内无热燥者，非火证也；外无寒热者，非表邪也。无食无火而忽为呕吐者，胃虚也；呕吐无常而时作时止者，胃虚也；食无所停而闻食则呕者，胃虚也；气无所逆而闻气则呕者，胃虚也；或身背、或食饮微寒即呕者，胃虚也；或吞酸，或嗳腐，时苦恶心，兀兀然、泛泛然冷咽靡宁者，胃虚也；或因病误治，妄用克伐寒凉，本无呕而致呕者，胃虚也；或朝食暮吐，暮食朝吐，食人中焦而不化者，胃虚也；食入下焦而不化者，土母无阳，命门虚也。治宜温补。",
    //     "id": 1
    // }`
  },
  {
    title: () => t('datasets.qa.acu.title'),
    description: () => t('datasets.qa.acu.desc'),
    githubLink: '',
    columns: qaColumns,
    data: acuData, // Placeholder
    codeExample: JSON.stringify(acuData[0], null, 2) // 将 acupuncture 问答数据的第一条记录格式化为 JSON 字符串，用于代码示例展示
  },
  {
    title: () => t('datasets.qa.mra.title'),
    description: () => t('datasets.qa.mra.desc'),
    githubLink: '',
    columns: mraColumns,
    data: mraData, // Placeholder
    scrollX: 1500,
    codeExample: JSON.stringify(mraData[0], null, 2) // 将病案分析问答数据的第一条记录格式化为 JSON 字符串，用于代码示例展示
  },
  // Choice Sections
  {
    title: () => t('datasets.choice.a1.title'),
    description: () => t('datasets.choice.a1.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A1.json',
    columns: choiceColumns,
    data: a1Data,
    codeExample: JSON.stringify(a1Data[0], null, 2) // 将 A1 数据的第一条记录格式化为 JSON 字符串，用于代码示例展示
  },
  {
    title: () => t('datasets.choice.a2.title'),
    description: () => t('datasets.choice.a2.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A2.json',
    columns: choiceColumns,
    data: a2Data,
    codeExample: JSON.stringify(a2Data[0], null, 2) // 将 A2 数据的第一条记录格式化为 JSON 字符串，用于代码示例展示
  },
  {
    title: () => t('datasets.choice.a3.title'),
    description: () => t('datasets.choice.a3.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A3.json',
    columns: [...a3a4Columns],
    data: a3Data,
    codeExample: JSON.stringify(a3Data[0], null, 2) // 将 A3 数据的第一条记录格式化为 JSON 字符串，用于代码示例展示
  },
  {
    title: () => t('datasets.choice.a4.title'),
    description: () => t('datasets.choice.a4.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A4.json',
    columns: [...a3a4Columns],
    data: a4Data, // Placeholder
    codeExample: JSON.stringify(a4Data[0], null, 2) // 将 A4 数据的第一条记录格式化为 JSON 字符串，用于代码示例展示
  },
  {
    title: () => t('datasets.choice.b.title'),
    description: () => t('datasets.choice.b.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/B.json',
    columns: [...bColumns],
    data: bData, // Placeholder
    codeExample: JSON.stringify(bData[0], null, 2) // 将 B 数据的第一条记录格式化为 JSON 字符串，用于代码示例展示
  },
  {
    title: () => t('datasets.choice.x.title'),
    description: () => t('datasets.choice.x.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/X.json',
    columns: choiceColumns,
    data: xData, // Placeholder
    codeExample: JSON.stringify(xData[0], null, 2) // 将 X 数据的第一条记录格式化为 JSON 字符串，用于代码示例展示
  }
])
</script>
