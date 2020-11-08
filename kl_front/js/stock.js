define([
    'echarts', 
    'apiUtil',
    'k-line',
    'k-type'
], function(echarts, Api, Line, KUrl) {
    var kChart = echarts.init(document.getElementById('main'));
    var stockParam = {
        asset_code: 'sh',
        ktype: 'D'
    }
    /**
     * K线图初始化
     */
    function kInit() {
        kstock(stockParam);
    }
    /**
     * 导航
     * @param {object} param fa 父元素  list 导航条数据
     */
    function navInit (param) {
        var nav = new Nav(param).init();
    }
    var Nav = function (param) {
        this.fa = param.fa;
        this.navLi = param.list
    }
    Nav.prototype = {
        // 初始化
        init: function () {
            let _this = this
            this.navLi.forEach(function(item, i) {
                var na = $('<div data-type="' + item.type + '">' + item.text + '</div>');
                if (i === 0) na.addClass('active'); 
                _this.fa.append(na);
            });
            // 事件绑定
            this.eventbind();

            return this;
        },
        // 事件绑定
        eventbind: function () {
            let _this = this;
            this.fa.on('click', 'div', function () {
                _this.fa.find('.active').removeClass('active');
                $(this).addClass('active');
                stockParam.ktype = $(this).attr('data-type');
                console.log(stockParam);
                kstock(stockParam);
            });
        }
    }
    /**
     * 股票数据请求
     * @param {object} param  asset_code ktype
     */
    function kstock(param) {
        Api.asynGetdata(KUrl.klUrl().kl, {
            asset_code: param.asset_code,
            ktype: param.ktype
        }).then(function (res) {
            console.log(res);
            var kline = res.data;
            $('.stock-title').html(res.title);
            kChart.setOption(Line.initKOption(kline));
        });
    }
    /**
     * 搜索股票结果
     * @param { Object } param  fa  父元素
     */
    var Stock = function (param) {
        this.fa = param.fa;
        this.stockList = [];
        this.ul = $('<ul class="search-list"></ul>')
    }
    Stock.prototype = {
        // 初始化
        init: function () {
            this.fa.append(this.ul);
            // 事件绑定
            this.eventbind();

            return this;
        },
        addList: function (data) {
            let _this = this;
            this.ul.find('li').remove();
            this.stockList = data;
            if (this.stockList.length <= 0) return;
            this.stockList.forEach(function(item,i) {
                var li = $('<li data-code="' + item.code + '">' + item.name + '</li>');

                _this.ul.append(li);
            });

            this.show();

            return this;
        },
        // 显示
        show: function () {
            this.ul.fadeIn(); 

            return this;
        },
        // 隐藏
        hide: function () {
            this.ul.hide();

            return this;
        },
        // 事件绑定
        eventbind: function () {
            let _this = this;
            this.fa.on('click', 'ul li', function () {
                stockParam.asset_code = $(this).attr('data-code');
                stockParam.ktype = 'D';
                $('.info-nav').find('.active').removeClass('active');
                $('.info-nav').find('div').eq(0).addClass('active');
                kstock(stockParam);
                _this.hide();
            });
            this.fa.on('click', function (e) {
                if (e.stopPropagation) 
                    e.stopPropagation();       // 停止冒泡  非ie
                else
                    e.cancelBubble = true;    // 停止冒泡 ie
            });
            $(document).on('click', function () {
                _this.hide();
            });
        }
    }
    
    return {
        kInit: kInit,
        navInit: navInit,
        stock: Stock,
    }
});