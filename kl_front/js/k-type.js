define([
    'jquery'
], function($) {
    var typeUrl = [
        {   // 股票
            query: 'query_stock',
            kl: 'stock_k_data'
        },
        {   // 期货
            query: 'query_future',
            kl: 'future_k_data'
        }
    ]
    var tyI = 0
    var klUrl = typeUrl[tyI]
    $('.kl-type').on('click', 'li', function () {
        if ($(this).index() == tyI) return
        tyI = $(this).index();
        $(this).parent().find('.active').removeClass('active');
        $(this).addClass('active');
        klUrl = typeUrl[tyI];
    })
    
    return {
        klUrl: function () {
            return klUrl
        }
    }
});