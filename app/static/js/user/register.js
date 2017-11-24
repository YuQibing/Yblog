/**
 * Created by yuqibing on 24/11/2017.
 */
$(function () {
        $('#freshCode').bind('click', function () {
            var getTimestamp=new Date().getTime();
            console.log('click')
            $('#verifyCode').attr('src','/user/Verify?time=' + getTimestamp)
        })
})

