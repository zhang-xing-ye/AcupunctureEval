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
  { id: 2, question: "劳瘿是什么，由什么引起，出自哪本书，孙思邈如何分类和治疗？", answer: "劳瘿为病证名，指瘿病由情绪刺激引起者，出《备急千金要方》卷二十四。孙思邈将瘿分为石瘿、气瘿、劳瘿、土瘿与忧瘿五种，并处五瘿丸以治疗之，即“取鹿靥以佳酒浸令没，炙干，纳酒中更炙，令香，含咽汁，味尽更易，尽十具愈。”" },
  { id: 3, question: "流泪·肺虚风袭证的症状有哪些？", answer: "流泪·肺虚风袭证（lacrimation with pattern of lung deficiency and wind invasion）是指肺虚风袭，以目无赤痛，冷泪迎风而出，或见咳喘无力，声音低怯，自汗畏风，神疲乏力，舌质淡胖，苔薄白，脉细弱为常见症的流泪症证候。" },
  { id: 4, question: "气瘤·脾虚痰凝证和气瘤·肝气郁结证的症状分别是什么？", answer: "气瘤·脾虚痰凝证是指脾虚痰凝，以气瘤多且根稍深，质软，无触痛，或得温稍舒，伴头身困重，口淡不渴，口黏无味，腹胀便溏等全身症状为常见症的气瘤证候。气瘤·肝气郁结证是指肝气郁结，以肿块质地较坚硬，按之韧实，活动度较差，表皮颜色一般不改变，局部有反射性酸麻胀感，或有较严重的疼痛，肿块可随情绪变化而增大或缩小，伴烦躁、易怒、咽干、失眠，舌苔微黄，舌质红，脉细弦为常见症的气瘤证候。" },
  { id: 5, question: "水肿的治疗方法有哪些，针灸治疗本证有什么效果？", answer: "水肿的治疗方法有发汗、利尿、攻逐、健脾、温肾、降浊、化瘀等。如经一般常法治疗不应，或有瘀血征象者，可参合应用活血化瘀法。以上诸法，或单用，或合用，均视病情需要而选择。针灸治疗本证有一定效果，在改善症状、增强体质、减少反复发作等方面有较好的疗效。" }
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
  {
    "question": "如何治疗足少阳经筋的病症？",
    "answer": "治疗足少阳经筋的病症以火针劫刺，并以痛为腧，即根据疼痛部位进行针刺治疗。这一治疗方法直接摘自文本注解部分，强调了对经筋病症的传统针灸疗法。",
    "id": 3
  },
  {
    "question": "清冷渊穴的穴位解剖结构是什么？",
    "answer": "清冷渊穴的穴位解剖结构为：穴下依次为皮肤、皮下组织、肱三头肌。有中侧副动、静脉末支分布，神经分布包括臂背侧皮神经和桡神经肌支。皮肤由桡神经发出的臂后皮神经分布，深层有中副动、静脉和桡神经肌支等。浅层有臂背侧皮神经和臂内侧皮神经分布，深层有桡神经肌支和肱深动脉分布。",
    "id": 4
  },
  {
    "question": "后顶穴主治哪些病证？",
    "answer": "后顶穴主要治疗头目及神志等疾患，如头昏目眩，癫痫及头项强急，历节汗出，烦心，头痛，眩晕，癫狂痫，头顶痛，颈项强痛，风眩目眩，癫狂，痫证，瘛疭，目视不明，外感热病，咽喉疼痛，目眩，失眠，癔病，现代又用以治疗感冒，偏头痛，神经性头痛，精神病，颈项肌肉痉挛，精神分裂症等。",
    "id": 5
  }
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
  {
    "ID": "经闭_病案分析题_1",
    "type": "病案分析题",
    "question": "吴某，女，32岁。未婚。主诉：停经1年。患者长期居住在阴冷潮湿之地，平素怕冷。1年前无明显诱因出现月经停止来潮，服用中药、西药（用药不详）治疗后，月经仍未来潮，今为求进一步诊治来针灸科门诊就诊。现症见手足冰凉，小腹轻微冷痛，小便少，舌淡，苔薄白，脉沉迟。请写出本病的病因病机、诊断、证型、治法、处方及方义。",
    "etiology and pathogenesis": "寒凝胞宫，滞而不通。",
    "diagnose": "经闭",
    "syndromes": "血滞经闭—寒凝胞宫证",
    "therapy": "温暖胞宫，通调冲任，活血通经。以任脉及足太阴、手阳明经穴为主。",
    "prescription": "中极、血海、三阴交、合谷、子宫、命门、神阙",
    "meaning of prescriptions": "血海、合谷、三阴交活血通经，三穴活血化瘀作用明显，同用可使气血、冲任调和，经闭可通；中极能调理冲任，疏通下焦；命门为督脉穴位，督脉总督一身之阳经，可补阳气；子宫和神阙都为近部取穴，温灸可达温暖胞宫的作用。诸穴合用，共奏温暖胞宫、通调冲任、活血通经之效。",
    "operation": "毫针泻法，可加艾灸或隔姜灸，每日1次，10次为一疗程。",
    "id": 3
  },
  {
    "ID": "痛经_病案分析题_1",
    "type": "病案分析题",
    "question": "李某，女，32岁。主诉：经期腹痛2年余。自述每次月经来潮前几天开始小腹疼痛，服用止痛药效果欠佳，严重时需注射杜冷丁止痛。2天前患者出现小腹疼痛，服用止痛药缓解。今晨患者月经来潮，伴小腹疼痛难忍，服用止痛药未缓解，遂来针灸科门诊就诊。现症见小腹冷痛，喜温暖，月经量少，有血块，舌暗有瘀点，脉沉涩。请写出本病的病因病机、诊断、证型、治法、处方及方义。",
    "etiology and pathogenesis": "冲任瘀阻，血行不畅，胞宫经血流通受阻，不通则痛。",
    "diagnose": "痛经",
    "syndromes": "寒凝血瘀证",
    "therapy": "温经散寒，活血止痛。以任脉、足太阴经为主。",
    "prescription": "中极、三阴交、地机、次髎、十七椎、关元、归来",
    "meaning of prescriptions": "中极可通调冲任，理下焦之气；三阴交能调理肝、脾、肾，活血止痛；地机为脾经郄穴，善于止痛治血，取之能行气活血止痛；次髎与十七椎为治疗痛经的经验效穴；关元是任脉与足三阴经的交会穴，可以调理肝肾、温养冲任；归来位于下腹部，具有活血调经的作用。诸穴合用，共奏温经散寒、活血止痛之效。",
    "operation": "毫针泻法，可加艾灸或隔姜灸，每日1次，月经前5～7日开始，连续3个月经周期。",
    "id": 4
  },
  {
    "ID": "月经不调_病案分析题_1",
    "type": "病案分析题",
    "question": "张某，女，27岁。主诉：月经提前1周。患者1年前开始出现月经提前，服用中药（具体不详）后好转，后在疲劳、熬夜后加重。2天前，患者月经提前1周来潮，经量少，色红质稠，两颧潮红、手足心热，舌红，苔少，脉细数。请写出本病的病因病机、诊断、证型、治法、处方及方义。",
    "etiology and pathogenesis": "虚热内生，热伏冲任，血海不宁。",
    "diagnose": "月经先期",
    "syndromes": "虚热证",
    "therapy": "养阴清热，凉血调经。以任脉及足太阴经穴为主。",
    "prescription": "关元、血海、三阴交、地机、太溪",
    "meaning of prescriptions": "关元可补下焦真元而化生精血；血海可以补血养血；三阴交能调理肝、脾、肾，可补血统血；地机穴为脾经郄穴，有活血化瘀之功；太溪为肾的原穴，有壮水制火的作用。诸穴合用可共奏养阴清热、凉血调经之效。",
    "operation": "毫针平补平泻，每日1次，每次留针20～30 min，10次为一疗程。",
    "id": 5
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
  {
    "ID": "3",
    "question": "剑胸结合中点至脐中的骨度分寸是（ ）",
    "options": [
      "A.6寸",
      "B.7寸",
      "C.8寸",
      "D.9寸",
      "E.12寸"
    ]
  },
  {
    "ID": "4",
    "question": "手少阴心经的终止穴是（ ）",
    "options": [
      "A.少商",
      "B.少泽",
      "C.少冲",
      "D.商阳",
      "E.至阴"
    ]
  },
  {
    "ID": "5",
    "question": "治疗急性胃痛常选取（ ）",
    "options": [
      "A.梁门",
      "B.梁丘",
      "C.公孙",
      "D.足三里",
      "E.天枢"
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
  {
    "ID": "3",
    "question": "郁证的基本病机是（ ）",
    "options": [
      "A. 痰气郁结，蒙蔽清窍",
      "B. 气机郁滞，脏腑阴阳气血失调",
      "C. 髓海不足，神机失用",
      "D. 痰热动风，脑神被扰",
      "E. 痰火上扰，神志逆乱"
    ]
  },
  {
    "ID": "4",
    "question": "不寐的基本治法是（ ）",
    "options": [
      "A. 调和阴阳，安神利眠",
      "B. 补益肝肾，安神助眠",
      "C. 调理心脾，安神助眠",
      "D. 益气养血，安神利眠",
      "E. 交通心肾，安神利眠"
    ]
  },
  {
    "ID": "5",
    "question": "与牙痛密切相关的脏腑是（ ）",
    "options": [
      "A. 心、脾",
      "B. 脾、胃",
      "C. 肾、胃",
      "D. 脾、肾",
      "E. 心、肾"
    ]
  }
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
  {
    "ID": "B_2",
    "Shared Option": [
      "A. 两肘",
      "B. 两腋",
      "C. 两髀",
      "D. 两胭",
      "E. 两肩"
    ],
    "questions": [
      {
        "question": "肝有邪，其气留于（ ）"
      },
      {
        "question": "肾有邪，其气留于（ ）"
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
  {
    "ID": "3",
    "question": "下列各项中，足三阳经共同的主治病症有（ ）",
    "options": [
      "A. 热病",
      "B. 头面五官病",
      "C. 胃肠病",
      "D. 神志病",
      "E. 妇科病"
    ]
  },
  {
    "ID": "4",
    "question": "火针的作用包括（ ）",
    "options": [
      "A. 温经散寒",
      "B. 活血化瘀",
      "C. 软坚散结",
      "D. 祛腐生肌",
      "E. 开窍泻热"
    ]
  },
  {
    "ID": "5",
    "question": "疏密波常用于治疗下列哪些疾病（ ）",
    "options": [
      "A. 痛症",
      "B. 软组织损伤",
      "C. 关节周围炎",
      "D. 局部冻伤",
      "E. 面瘫"
    ]
  }
]
const sections = ref([
  // QA Sections
  {
    title: () => t('datasets.qa.tcm.title'),
    description: () => t('datasets.qa.tcm.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Clin/CMB-Clin.json',
    columns: qaColumns,
    data: tcmData,
    codeExample: `
  {
    "question": "什么是虚呕？",
    "answer": "虚呕是指脾胃虚弱，胃失和降，胃气上逆所致的呕吐。发病缓慢，病程较长。《景岳全书·杂证谟》：凡胃虚作呕者，其证不一，当知所辨。若胃脘不胀者，非实邪也；胸膈不痛者，非气逆也；内无热燥者，非火证也；外无寒热者，非表邪也。无食无火而忽为呕吐者，胃虚也；呕吐无常而时作时止者，胃虚也；食无所停而闻食则呕者，胃虚也；气无所逆而闻气则呕者，胃虚也；或身背、或食饮微寒即呕者，胃虚也；或吞酸，或嗳腐，时苦恶心，兀兀然、泛泛然冷咽靡宁者，胃虚也；或因病误治，妄用克伐寒凉，本无呕而致呕者，胃虚也；或朝食暮吐，暮食朝吐，食人中焦而不化者，胃虚也；食入下焦而不化者，土母无阳，命门虚也。治宜温补。",
    "id": 1
}`
  },
  {
    title: () => t('datasets.qa.acu.title'),
    description: () => t('datasets.qa.acu.desc'),
    githubLink: '',
    columns: qaColumns,
    data: acuData, // Placeholder
    codeExample: `
  {
    "question": "足少阳络脉的起点和路径是怎样的？",
    "answer": "足少阳络脉的起点和路径为：脉自外踝上5寸处的光明穴分出，走向足厥阴经脉以沟通表里两经，再向下络于足背，这一详细描述来自注解中参见足少阳络脉的部分。",
    "id": 1
}`
  },
  {
    title: () => t('datasets.qa.mra.title'),
    description: () => t('datasets.qa.mra.desc'),
    githubLink: '',
    columns: mraColumns,
    data: mraData, // Placeholder
    scrollX: 1500,
    codeExample: `
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
}`
  },
  // Choice Sections
  {
    title: () => t('datasets.choice.a1.title'),
    description: () => t('datasets.choice.a1.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A1.json',
    columns: choiceColumns,
    data: a1Data,
    codeExample: `
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
},`
  },
  {
    title: () => t('datasets.choice.a2.title'),
    description: () => t('datasets.choice.a2.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A2.json',
    columns: choiceColumns,
    data: a2Data,
    codeExample: `
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
},`
  },
  {
    title: () => t('datasets.choice.a3.title'),
    description: () => t('datasets.choice.a3.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A3.json',
    columns: [...a3a4Columns],
    data: a3Data,
    codeExample: `
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
    },`
  },
  {
    title: () => t('datasets.choice.a4.title'),
    description: () => t('datasets.choice.a4.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/A4.json',
    columns: [...a3a4Columns],
    data: a4Data, // Placeholder
    codeExample: `
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
},`
  },
  {
    title: () => t('datasets.choice.b.title'),
    description: () => t('datasets.choice.b.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/B.json',
    columns: [...bColumns],
    data: bData, // Placeholder
    codeExample: `
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
},`
  },
  {
    title: () => t('datasets.choice.x.title'),
    description: () => t('datasets.choice.x.desc'),
    githubLink: 'https://github.com/FreedomIntelligence/CMB/blob/master/data/CMB-Exam/CMB-test/X.json',
    columns: choiceColumns,
    data: xData, // Placeholder
    codeExample: `
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
},`
  }
])
</script>
