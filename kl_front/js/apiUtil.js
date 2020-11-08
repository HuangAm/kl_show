define([
    'jquery',
    'promise'
], function() {
    var AsynGetdata = function(router, params, type) {
        // var mainUrl = "http://886fx.com/api/";
        var mainUrl = "http://127.0.0.1:8889";
        var promise = new Promise(function(resolve, reject) {
          $.ajax({
            type: type ? type : "post",
            url: mainUrl + router,
            data: params,
            headers: {
              "Content-type": "application/x-www-form-urlencoded"
            },
            success: function(res) {
              if (res.status == "200") {
                resolve(res);
              } else {
                new Hint({
                  context: res.message
                }).init();
                reject(res);
              }
            },
            error: function(err) {
              console.log(err);
            }
          });
        });
        return promise;
    }
    /**
     * 提示
     * @param {Object} 
     */
    var Hint = function(data) {
        this.box = $("<div class='hint'></div>");
        this.context = data.context ? data.context : "错误";
        this.duration = data.duration ? data.duration : "2000";
    };
    Hint.prototype = {
        // 初始化
        init: function() {
            // 插入提示内容
            this.box.text(this.context);
            // 显示
            this.show();
        },
        // 显示
        show: function() {
            // 清除已有的
            $(".hint").remove();
            // 添加元素
            $("body").append(this.box);
            // this.duration 后消失
            this.hide();
        },
        // 消失
        hide: function() {
            var _this = this;
            this.timer = setTimeout(function() {
                _this.box.remove();
            }, this.duration);
        }
    };

    // var hintPop = function (param) {
    //   new Hint(param).init();
    // }

    return {
        asynGetdata: AsynGetdata,
        hint: Hint
    }
});