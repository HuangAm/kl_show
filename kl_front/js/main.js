requirejs.config({
    baseurl: 'js',
    paths: {
        jquery: '../src/jquery-3.2.1.min',
        promise: '../src/promise',
        echarts: '../src/echarts.min'
    }
});

require(['jquery', 'apiUtil', 'stock', 'k-type'], function ($, Api, Stock, KUrl) {
    // 判断PC
    if (IsPC()) {
        $('.info').addClass('info-pc');
        $('.canvas').addClass('canvas-pc');
    }
    // 导航初始化
    var navList = [
        { type: 'D', text: '日K' },
        { type: '5', text: '5分' },
        { type: '15', text: '15分' },
        { type: '30', text: '30分' },
    ];
    Stock.navInit({fa: $('.info .info-nav'), list: navList});
    // k线初始化
    Stock.kInit();
    // 初始化搜索列表
    var stock = new Stock.stock({
        fa: $('.info .info-search')
    }).init();

    /**
     * 搜索
     */
    $('.serach-ipt').on('input', function (e) {
        console.log(KUrl.klUrl());
        var val = e.target.value;
        if (val === '') return
        Api.asynGetdata(KUrl.klUrl().query, {
            query_str: val
        }).then(function (res) {
            console.log(res)
            if (res.data.length <= 0) return
            stock.addList(res.data)
        });
    }).on('focus', function() {
        if (stock.ul.find('li').length <= 0) return
        stock.show();
    });
    
    /**
     * 判断是否PC端
     */
    function IsPC() {
        var userAgentInfo = navigator.userAgent;
        var Agents = ["Android", "iPhone",
            "SymbianOS", "Windows Phone",
            "iPad", "iPod"];
        var flag = true;
        for (var v = 0; v < Agents.length; v++) {
            if (userAgentInfo.indexOf(Agents[v]) > 0) {
                flag = false;
                break;
            }
        }
        return flag;
    }
});