/* -----------------时间图-------------------   */
var MonthBar = echarts.init(document.getElementById('month_bar'));
var MonthBar2 = echarts.init(document.getElementById('month_bar2'));
var optionMonthBar = {
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [120, 200, 150, 80, 70, 110, 130],
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
        }
    }]
};    
MonthBar.setOption(optionMonthBar);
MonthBar2.setOption(optionMonthBar);

var WeekBar = echarts.init(document.getElementById('week_bar'));
var WeekBar2 = echarts.init(document.getElementById('week_bar2'));
var optionWeekBar = {
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [10, 5, 8, 7, 6, 9, 8],
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
        }
    }]
};    
WeekBar.setOption(optionWeekBar);
WeekBar2.setOption(optionWeekBar);

var DayBar = echarts.init(document.getElementById('day_bar'));
var DayBar2 = echarts.init(document.getElementById('day_bar2'));
var optionDayBar = {
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [120, 200, 150, 80, 70, 110, 130],
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
        }
    }]
};    
DayBar.setOption(optionDayBar);
DayBar2.setOption(optionDayBar);



/* -----------------饼图-------------------   */

var SubPie = echarts.init(document.getElementById('subproject_pie'));
var SubPie2 = echarts.init(document.getElementById('subproject_pie2'));
var optionSubPie ={
    // title: {
    //     text: '任务分配图',
    //     // subtext: '纯属虚构',
    //     left: 'center'
    // },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        orient: 'horizontal',
        bottom: '2',
    },
    series: [
        {
            name: '任务分配',
            type: 'pie',
            radius: '50%',
            center: ['50%', '40%'],
            label: {
                show:false
            },
            data: [
                {value: 1048, name: '数学'},
                {value: 735, name: '语文'},
                {value: 580, name: '邮件营销'},
                {value: 484, name: '联盟广告'},
                {value: 300, name: '视频广告'}
            ],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
SubPie.setOption(optionSubPie);
SubPie2.setOption(optionSubPie);
