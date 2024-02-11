$(document).ready(function() {
    $('#switch').click(function() {
        $.ajax({
            url: '/ajax/',
            type: 'GET',
            success: function(response){
                if ($('#switch').hasClass('make_account')) {
                    $('.account').html('Вже маєте акаунт?')
                    $('#switch').html('Ввійти в акаунт')
                    $('#switch').removeClass('make_account')
                    $('#switch').addClass('have_account')
                    $('.form').append(
                        `<label for="first_name" class='first_name'>First name</label>
                        <input type="text" name="first_name" id="first_name" class="first_name">`
                    )
                    $('#send').removeClass('log')
                    $('#send').addClass('reg')
                    $('#error').remove()
                } 
                else if ($('#switch').hasClass('have_account')) {
                    $('.account').html('Немає акаунту?')
                    $('#switch').html("Зробити акаунт")
                    $('#switch').removeClass('have_account')
                    $('#switch').addClass('make_account')
                    $('.first_name').remove()
                    $('#send').removeClass('reg')
                    $('#send').addClass('log')
                    $('#error').remove()
                }
            }
        })
    })
})

$(document).ready(function(){
    $('.log').click(function(){
        if ($('#send').hasClass('log')){
            $.ajax({
                url: '/ajax/',
                type: 'POST',
                data: {
                    login: $('#login').val(),
                    password: $('#password').val(),
                    type: 'log'
                },
                success: function(response){
                    if (!response['error']){
                        window.location.replace('/main/')

                    } else if (response['error']){
                        $('.error').append(
                            `<p id='error'>${response['error']}</p>`
                        )
                    }
                }
            })
        } else if ($('#send').hasClass('reg')) {
            $.ajax({
                url: '/ajax/',
                type: 'POST',
                data: {
                    login: $('#login').val(),
                    password: $('#password').val(),
                    first_name: $('#first_name').val(),
                    type: 'reg'
                },
                success: function(response){
                    if (!response['error']){
                        $('.account').html('Немає акаунту?')
                        $('#switch').html("Зробити акаунт")
                        $('#switch').removeClass('have_account')
                        $('#switch').addClass('make_account')
                        $('.first_name').remove()
                        // $('#login').remove()
                        // $('#password').remove()
                        // $('#login_label').remove()
                        // $('#password_label').remove()
                        // $('.form').append(
                        //     `<label for="login">Login</label>
                        //     <input type="text" name="login" id="login">
                        //     <label for="password">Password</label>
                        //     <input type="password" name="password" id="password">`
                        // )
                        $('#send').removeClass('reg')
                        $('#send').addClass('log')

                    } else if (response['error']){
                        $('.error').append(
                            `<p id='error'>${response['error']}</p>`
                        )
                    }
                }
            })
        }
    })
})