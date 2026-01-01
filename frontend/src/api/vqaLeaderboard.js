import request from '@/utils/request'

export const getVqaLeaderboard = (params) => {
    return request({
        url: '/vqa/data',
        method: 'get',
        params
    })
}
export const vqaEvaluate = (data) => {
    return request({
        url: '/vqa/evaluate',
        method: 'post',
        data,
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
}
