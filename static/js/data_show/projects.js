
function getVirtulData(year) {
    year = year || '2017';
    var date = +echarts.number.parseDate(year + '-01-01');
    var end = +echarts.number.parseDate((+year + 1) + '-01-01');
    var dayTime = 3600 * 24 * 1000;
    var data = [];
    for (var time = date; time < end; time += dayTime) {
        data.push([
            echarts.format.formatTime('yyyy-MM-dd', time),
            Math.floor(Math.random() * 1000)
        ]);
    }
    console.log(data[data.length - 1]);
    return data;
}

var Calender = echarts.init(document.getElementById('calender'));
var Calender2 = echarts.init(document.getElementById('calender2'));
var optionCalender = {
    tooltip: {
        position: 'top'
    },

    visualMap: [{
        min: 0,
        max: 1000,
        show: false,
        calculable: true,
        seriesIndex: [0],
        orient: 'horizontal',
        left: 'center',
    },
    ],

    calendar: [
    {
        orient: 'vertical',
        top: 80,
        left: 20,
        yearLabel: {
            margin: 40
        },
        dayLabel: {
            firstDay: 1,
            nameMap: ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
        },
        monthLabel: {
            nameMap: 'cn',
            margin: 20
        },
        cellSize: 40,
        range: '2017-04',
    }],

    series: [{
        type: 'effectScatter',
        coordinateSystem: 'calendar',
        calendarIndex: 0,
        symbolSize: function (val) {
            return val[1] / 40;
        },
        data: getVirtulData(2017)
    }]
};

Calender.setOption(optionCalender);
Calender2.setOption(optionCalender);
