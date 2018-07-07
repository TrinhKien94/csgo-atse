var bet_color=1;
var lose_continue=0;
var max_lose = 0;
var lose_log = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
function convert_1_2(number){
    switch(number){
        case 1:
            return 2;
        default:
            return 1;
    }
}
function getHistory(){
	var len = $("#bets-list tr").length;
	var prev="";
	for(var i=1; i<= len; i++){
		var value=0;
		var profit =0;
		
		value=$("#bets-list tr:nth-child("+i+") td.value")[0].innerText;
		if($("#bets-list tr:nth-child("+i+") td.lose").length>0){
			profit=$("#bets-list tr:nth-child("+i+") td.lose")[0].innerText;
		}else{
			profit=$("#bets-list tr:nth-child("+i+") td.win")[0].innerText;
		}
		prev += value + '|' + profit+'|';
	}
	prev = prev.slice(0, -1);
// 	console.log(prev);
	return prev;
}
function show_lose_log(){
    var len = lose_log.length
    for(var i = 0; i < len; i++){
        console.log("Lose "+ i + " "+ lose_log[i]);
    }
}
function fisrtKick(){
    var myData = {'prev':getHistory()};
    $.ajax({
        type: "GET",
        data: myData,
        url: "http://127.0.0.1:5003/employees",
        dataType: "json",
        async: false,
        success: function(data){
            // console.log(data.predict.trim)
            bet_color = parseInt(data.predict);
            console.log('predict color: '+parseInt(data.predict));
            // console.log('percent win: '+data.percent);
            // console.log('total: '+parseInt(data.total));
        }
        
    });
}
service['coinflip'].history=function(bet) {
    // console.log("betd: "+bet_color);
    // console.log("amount: "+bet.amount);
    // console.log("profit: "+bet.profit);
    var option = parseInt(bet.option);
    var profit = parseInt(bet.profit);
    if(profit < 0){
        option = convert_1_2(option);
    }
    if(option != bet_color){
        console.log("Lose:"+(option)+"  predicted: "+bet_color);
    }else{
        console.log("Win:"+(option)+"  predicted: "+bet_color);
    }
    bet.prev=getHistory();
    if(bet_color != option){
        lose_continue+=1;
        console.log("lose_continue: "+lose_continue);
    }else{
        if(lose_continue > max_lose)
            max_lose = lose_continue;
        lose_log[lose_continue]+=1;
        lose_continue = 0;
    }
    $.ajax({
        type: "GET",
        data: bet,
        url: "http://127.0.0.1:5003/employees",
        dataType: "json",
        async: false,
        success: function(data){
            // console.log(data.predict.trim)
            bet_color = parseInt(data.predict);
            console.log('predict color: '+parseInt(data.predict));
            // console.log('percent win: '+data.percent);
            // console.log('total: '+parseInt(data.total));
        }
        
    });
    $('#bets-list tr').slice(14, 15).remove();
    $(tmpl('history-tpl', bet)).css({
        opacity: 0
    }).prependTo('#bets-list').animate({
        opacity: 1
    }, 200);
};
function getHistoryRoulette(){
	var len = $(".list .coin").length;
	var prev = $('.list .coin')[len-1].className.split(" ")[1]+"|"+$('.list .coin')[len-1].innerText;
	for(var i = len-2; i>=0;i--){
		prev+="|"+$('.list .coin')[i].className.split(" ")[1]+"|"+$('.list .coin')[i].innerText;
	}
	return prev;
}
service['roulette'].history=function(data) {
    console.log(data);
	// data.prev=getHistoryRoulette();
    // $.ajax({
    //     type: "GET",
    //     data: data,
    //     url: "http://127.0.0.1:5001/employees",
    //     dataType: "json",
    //     async: false,
    //     success: function(respone){
    //         console.log('predict color: '+respone.predict);
    //     }        
    // });
    $('<div class="coin ' + data.color + ' ' + (data.mega ? 'mega' : '') + '" title="' + data.id + ': ' + data.hash + '">' + data.value + '</div>').appendTo('.history .list').tooltipster({
        theme: 'tooltipster-light',
        animation: 'grow',
        delay: 0
    });
    if ($('.history:eq(0) .coin').length > 10) {
        $('.history .coin:eq(0)').remove();
    }
}
// service['roulette'].init = function() {
//     console.log("init");
//     let input = this.input;
//     let that = this;
//     if (user.theme === 'new') {
//         this.coin_width = 100;
//     }
//     this.centerize();
//     this.updateState();
//     $(window).resize(function() {
//         let width = $('.roll').width();
//         let change = (that.width - width) / 2;
//         that.width = width;
//         $('.roll .items', that.container).css({
//             backgroundPositionX: '-=' + change
//         });
//     });
//     $('.btn-bet', this.container).click(function() {
//         sounds.button.play();
//         let color = $(this).parents('.color').data('color');
//         let amount = parseFloat(input.val());
//         if (isNaN(amount)) {
//             return $.notify(T('Wrong amount'), 'error');
//         }
//         if (amount < bet_range[0]) {
//             return $.notify(T('Minimum bet amount is %d', bet_range[0]), 'error');
//         }
//         if (amount > Math.min(user.balance, bet_range[1])) {
//             return $.notify(T('Maximum bet amount is %d', Math.min(user.balance, bet_range[1])), 'error');
//         }
//         if (user.currency === 'usd') {
//             amount *= 1000;
//         }
//         amount = parseInt(amount);
//         if (user.balance === amount && Cookies.get('allIn') === 'false') {
//             $.popup('<div id="allIn" class="content"><h1>Are you sure you want to bet all your balance?</h1><br /><input type="submit" class="btn btn-accept accept" value="Yes" /><input type="submit" class="btn btn-decline decline" value="No" /></div>');
//             $('.btn-accept').click(function() {
//                 service['socket'].send({
//                     service: 'roulette',
//                     cmd: 'deposit',
//                     color: color,
//                     amount: amount
//                 });
//                 input.trigger('change');
//                 $('.popup').close();
//                 return true;
//             });
//             $('.btn-decline').click(function() {
//                 $('.popup').close();
//                 return false;
//             });
//             return false;
//         } else {
//             service['socket'].send({
//                 service: 'roulette',
//                 cmd: 'deposit',
//                 color: color,
//                 amount: amount
//             });
//             input.trigger('change');
//             return false;
//         }
//     });
//     $('.show-bets').click(function() {
//         $('body').addClass('show-bets');
//         $(this).parent().next('.list').addClass('opened');
//     });
//     $(".last-mega").on('animation', function() {
//         $(this).removeClass('last-mega-animation').width();
//         $(this).addClass('last-mega-animation');
//     });
//     this.lastMegaShake();
// }
// service['roulette'].round = function(data) {
//     console.log("round: ");
//     console.log(data)
//     this.megaStop();
//     this.built = false;
//     this.items = [];
//     this.bets = [];
//     this.yours = {
//         red: 0,
//         green: 0,
//         black: 0
//     };
//     this.summary = {
//         red: [],
//         green: [],
//         black: []
//     };
//     this.amount = 0;
//     this.start = null;
//     this.hash = '';
//     $('.color').removeClass('win lose');
//     /**
//                  @mobile-changes
//                  */ // $('.color .list', this.container).html('');
//     $('.profile', this.container).remove();
//     $(this.container).removeClass('round countdown draw winner');
//     $('.your .value', this.container).stop(true, true).animateNumber({
//         number: 0,
//         numberStep: currencyStep
//     });
//     $('.bets .sum .value', this.container).stop(true, true).animateNumber({
//         number: 0,
//         numberStep: currencyStep
//     });
//     $('.bets .sum .counter', this.container).stop(true, true).animateNumber({
//         number: 0,
//         numberStep: numberStep
//     });
//     this.container.addClass('round');
// }
// service['roulette'].info = function(data) {
//     console.log("info");
//     console.log(data)
//     this.state = data.state;
//     this.id = data.id;
//     if (data.hash) {
//         this.hash = data.hash;
//     }
//     if (data.secret) {
//         this.secret = data.secret;
//     }
//     if (data.value) {
//         this.value = data.value;
//     }
//     if (data.timer) {
//         this.timer = data.timer;
//     }
//     if (data.value) {
//         this.value = data.value;
//     }
//     if (data.color) {
//         this.color = data.color;
//     }
//     if (data.multiplier) {
//         this.multiplier = data.multiplier;
//     }
//     if (data.mega) {
//         this.mega = data.mega;
//     }
//     if (data.config) {
//         this.config = data.config;
//         setBetRange(data.config);
//     }
//     if (data.history) {
//         for (let i in data.history) {
//             this.history(data.history[i]);
//         }
//     }
//     if (data.bets) {
//         for (let i in data.bets) {
//             this.bet(data.bets[i], false);
//         }
//         let that = this;
//         $('.colors .color').each(function() {
//             that.recalculate($(this));
//         });
//     }
//     if (data.last_mega) {
//         $('.last-mega .value').text(data.last_mega);
//     }
//     this.updateState();
//     $('.hash', this.container).text(data.hash);
//     if (data.state === 'ROUND') {
//         this.round(data);
//     } else if (data.state === 'COUNTDOWN') {
//         this.countdown(data);
//     } else if (data.state === 'MEGAROUND') {
//         this.megaround(data);
//     } else if (data.state === 'DRAW') {
//         this.draw(data);
//     } else if (data.state === 'WINNER') {
//         this.winner(data);
//     }
// }
function getHistoryRoulette(){
	var len = $(".list .coin").length;
	var prev = $('.list .coin')[len-1].className.split(" ")[1]+"|"+$('.list .coin')[len-1].innerText.trim();
	for(var i = len-2; i>=0;i--){
		prev+="|"+$('.list .coin')[i].className.split(" ")[1]+"|"+$('.list .coin')[i].innerText.trim();
	}
	return prev;
}
service['roulette'].winner = function(data) {
    console.log('winner');
    console.log(data);
    let that = this;
    data.prev=getHistoryRoulette();
    $.ajax({
        type: "GET",
        data: data,
        url: "http://127.0.0.1:5001/employees",
        dataType: "json",
        async: false,
        success: function(respone){
            console.log('predict color: '+respone.predict);
        }        
    });
    $('.colors .color').each(function() {
        let sum = 0;
        let bet = 0;
        if ($(this).data('color') === that.color) {
            sum = arraySum(that.summary[that.color]) * that.multiplier;
            bet = that.yours[that.color] * that.multiplier;
            $(this).addClass('win');
        } else {
            $(this).addClass('lose');
            sum = arraySum(that.summary[$(this).data('color')]) * -1;
            bet = that.yours[$(this).data('color')] * -1;
        }
        $('.sum .value', this).stop(true, true).animateNumber({
            number: sum,
            numberStep: currencyStepSign
        }, 20);
        $('.your .value', this).stop(true, true).animateNumber({
            number: bet,
            numberStep: currencyStepSign
        }, 20);
    });
}