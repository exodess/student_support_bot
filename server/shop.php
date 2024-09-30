<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Магазинчик баллов</title>
	<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&family=Open+Sans:wght@400&display=swap" rel="stylesheet"> <!-- Подключаем шрифты из Google Fonts -->
    <style> 
        body {  
            font-family: 'Open Sans', sans-serif; /* Используем шрифт Open Sans для текста */  
            background: linear-gradient(to right, #e3f2fd, #bbdefb); /* Градиентный фон */ 
            margin: 0;  
            padding: 20px;  
            text-align: center;  
        }  
         
        h1 {  
            font-family: 'Poppins', sans-serif; /* Используем шрифт Poppins для заголовка */
            color: #1565c0; /* Цвет заголовка */ 
            margin-bottom: 30px;  
        } 
         
        div {  
            display: inline-block;  
            background: #ffffff; /* Белый фон для каждого товара */ 
            border-radius: 5px; /* Закругленные углы */ 
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Тень для блока */ 
            margin: 20px; /* Отступ между товарами */ 
            padding: 20px; /* Отступ внутри блока */ 
            transition: transform 0.3s; /* Плавный переход при наведении */ 
            border: 2px solid #ffccbc; /* Цветной бордер для каждого товара */ 
        }  
         
        div:hover {  
            transform: scale(1.05); /* Увеличение блока при наведении */ 
            border-color: #ffab40; /* Изменение цвета бордера при наведении */ 
        }  
         
        img {  
            border-radius: 5px; /* Скругленные углы для изображений */ 
            max-width: 100%; /* Адаптация по ширине родителя */ 
            height: auto; /* Автоматическая высота */ 
        }  
         
        h2, h3 {  
            color: #424242;  
            margin: 10px 0; /* Отступы между заголовками */ 
            font-family: 'Open Sans', sans-serif; /* Используем шрифт Open Sans для заголовков товаров */
        }  
         
        .btn {  
            display: inline-block;  
            background: #795548; /* Коричневая кнопка */  
            color: #fff; /* Белый цвет текста кнопки */  
            padding: 1rem 1.5rem; /* Поля вокруг текста кнопки */  
            text-decoration: none; /* Убираем подчёркивание */  
            border-radius: 3px; /* Скругляем уголки кнопки */  
            transition: background 0.3s, transform 0.2s; /* Плавный переход для кнопки */ 
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Тень для кнопки */ 
            font-family: 'Open Sans', sans-serif; /* Используем шрифт Open Sans для кнопок */
        }  
         
        .btn:hover {  
            background: #6d4c41; /* Более тёмный коричневый при наведении */  
            transform: scale(1.05); /* Увеличение кнопки */ 
        }  
    </style> 
    </head>
    <body>
        <h1>
            Выберите награду за свои баллы
        </h1>
        <?php
            $username = "Not found";
	    $IP_V4 = "http://192.168.0.161";
            if(isset($_GET["username"])){
                $username = $_GET["username"];
            }
            echo "<div>";
                echo "<img src='Rukzachok.png' width='300' height='300' alt='Рюкзачок-петушок'/>";
                echo "<h2>Рюкзачок-петушок для петушков)</h2>";
                echo "<h3>Цена - 1000 баллов</h3>";
		echo "<a href='$IP_V4/bot_project/buy.php?buy_code=1&username=$username' class='btn'>Обменять баллы на петушочка)</a>";

            echo "</div>";
            echo "<div>";
                echo "<img src='sertifikat.jpg' width='400' height='300' alt='Подарочный сертификат в читай-город'/>";
                echo "<h2>Подарочный сертификат в читай-город на 500 рублей</h2>";
                echo "<h3>Цена - 700 баллов</h3>";
		echo "<a href='$IP_V4/bot_project/buy.php?buy_code=2&username=$username' class='btn'>Обменять баллы на сертификат</a>";
            echo "</div>";
            echo "<div>";
                echo "<img src='shokoladka.jpg' width='300' height='300' alt='Шоколадка)'/>";
                echo "<h2>Вкуснейшая шоколадка дял сладкоежек :)</h2>";
                echo "<h3>Цена - 100 баллов</h3>";
		echo "<a href='$IP_V4/bot_project/buy.php?buy_code=3&username=$username' class='btn'>Обменять баллы на шоколадку</a>";
            echo "</div>";
            echo "<div>";
                echo "<img src='Socks.png' width='300' height='300' alt='Носочки'/>";
                echo "<h2>Носочки для самых стильных</h2>";
                echo "<h3>Цена - 400 баллов</h3>";
		echo "<a href='$IP_V4/bot_project/buy.php?buy_code=4&username=$username' class='btn'>Обменять баллы на стильные носочки</a>";
            echo "</div>";
            echo "<div>";
                echo "<img src='tea.jpg' width='250' height='300' alt='Чаёчек'/>";
                echo "<h2>Чаёчек согреет вас даже в самые холодные вечера</h2>";
                echo "<h3>Цена - 120 баллов</h3>";
		echo "<a href='$IP_V4/bot_project/buy.php?buy_code=5&username=$username' class='btn'>Обменять баллы на чаёчек</a>";
            echo "</div>";
        ?>
    </body>
</html>