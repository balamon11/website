# Ex.07 Restaurant Website
# Date:4/10/2025
# AIM:
To develop a static Restaurant website to display the food items and services provided by them.

# DESIGN STEPS:
## Step 1:
Requirement collection.

## Step 2:
Creating the layout using HTML and CSS.

## Step 3:
Updating the sample content.

## Step 4:
Choose the appropriate style and color scheme.

## Step 5:
Validate the layout in various browsers.

## Step 6:
Validate the HTML code.

## Step 7:
Publish the website in the given URL.

# PROGRAM:
 Views.py
 
     from django.shortcuts import render
    
    def home(request):
        return render(request,'home.html')
    def menu(request):
        return render(request,'menu.html')
    def admin(request):
        return render(request,'admin.html')
    def contact(request):
        return render(request,'contact.html')
 Urls.py
      
      from django.urls import path
     from app import views
     urlpatterns = [
         path('',views.home),
         path('menu/',views.menu),
         path('admin/',views.admin),
         path('contact/',views.contact),
     ]

 Home.html
 
    {% load static %}

    <html>
    <head>
        <style>

            body{
                background:linear-gradient(300deg,white,pink)
            }
            .head{
                color:black;
                text-shadow: 4px 4px 4px white;
                position:relative;
                top:35px;
            }
            .title{
                color:black;
                text-shadow: 4px 4px 4px white;
                position:aboslute;
                top:35px;
            }
            button{
                position:relative;
                top:40px;
                width:200px;
                height:50px;
                color:white;
                background:black;
            }
            img{
                height:100x;
                width:100px;
                position:relative;
                left:450px;
                top:-65px;

                
            }
        </style>



    </head>
    <body>
        <div class="head">
            <center><h1>Smoke Flying Chai Shop</h1></div></center>
            <img src={% static "chai.png" %} >
    <div class="title">
               <center>   <h1>Home</h1></center>

           <center> 
            <a href='/'><button>Home</button></a>

            <a href='/menu'><button>Menu</button></a>
           <a href='/admin'> <button>Administration</button></a>
           <a href='/contact'> <button>Contact Us</button></a>
    </div>


    <img src={% static "head1.png" %} style='top:500px; position:absolute;  left:150px;height:275px;width:1290px; border:3px solid black;border-radius:10px;'>
      

    <img src={% static "head2.png" %} style='top:500px; position:relative;  left:140px;height:600px;width:400px; border:3px solid black;border-radius:10px;'>

    <img src={% static "head3.png" %} style='top:500px; position:relative;  left:180px;height:600px;width:400px; border:3px solid black;border-radius:10px;'>

    <img src={% static "head4.png" %} style='top:500px; position:aboslute;  left:220px;height:600px;width:400px; border:3px solid black;border-radius:10px;'>



        </center>
       <center>        
       <h4 style='color:blue;position:relative;top:1000px;'> designed and developed by balaji<h4></center>

    </body>
    </html>
 Menu.html
  
    {% load static %}
      
      <html>
          <head>
              <style>
      
                  body{
                      background:linear-gradient(300deg,white,pink)
                  }
                  .head{
                      color:black;
                      text-shadow: 4px 4px 4px white;
                      position:relative;
                      top:35px;
                  }
                  .title{
                      color:black;
                      text-shadow: 4px 4px 4px white;
                      position:relative;
                      top:60px;
                  }
                  button{
                      position:relative;
                      top:40px;
                      width:200px;
                      height:50px;
                      color:white;
                      background:black;
                  }
                  .image{
                      height:100x;
                      width:100px;
                      position:relative;
                      left:450px;
                      top:-65px;
      
                      
                  }
                  .size1{
                  
      
                  }
              </style>
      
      
      
          </head>
          <body>
              <div class="head">
                  <center><h1>Smoke Flying Chai Shop</h1></div></center>
                  <div class="image"><img src={% static "chai.png" %} style='height:100x;
                      width:100px;
                      position:relative;
                      left:30px;
                      top:0px;' ></div>
      
      <center>   <h1>Menu</h1></center></div>
                 <center> 
                 <a href='/'><button>Home</button></a>
      
                  <a href='/menu'><button>Menu</button></a>
                 <a href='/admin'> <button>Administration</button></a>
                 <a href='/contact'> <button>Contact Us</button></a>
      <div class="title"
      
      <center>
      <img src={% static "1.png" %} style='top:100px; position:relative;  left:200px;height:200px;width:240px; border:3px solid black;border-radius:10px;'>
      
       <img src={% static "2.png" %} style='top:100px; position:relative; height:200px;width:240px; left:400px; border:3px solid black;border-radius:10px;' >
          
          
          <img src={% static "3.png" %} style='top:100px; position:relative;  left:600px; height:200px;width:240px;border:3px solid black;border-radius:10px;'>
       
          <img src={% static "4.png" %} style='top:400px; position:relative;  left:-550px;height:200px;width:240px; border:3px solid black;border-radius:10px;'>
      
          <img src={% static "5.png" %} style='top:400px; position:relative;  left:-360px;height:200px;width:240px; border:3px solid black;border-radius:10px;'>
          
          <img src={% static "6.png" %} style='top:400px; position:relative; height:200px;width:240px; left:-150px; border:3px solid black;border-radius:10px;' >
          
          
          <img src={% static "7.png" %} style='top:500px; position:relative;  left:190px;height:200px;width:240px; border:3px solid black;border-radius:10px;'>
          
          
        <img src={% static "8.png" %} style='top:500px; position:relative;  left:380px;height:200px;width:240px; border:3px solid black;border-radius:10px;'> 


    <img src={% static "9.png" %} style='top:500px; position:relative;  left: 600px;height:200px;width:240px; border:3px solid black;border-radius:10px;'>

    <img src={% static "10.png" %} style='top:800px; position:relative;  left:-560px;height:200px;width:240px; border:3px solid black;border-radius:10px;' >

    <img src={% static "11.png" %} style='top:800px; position:relative;  left:-360px;height:200px;width:240px; border:3px solid black;border-radius:10px;'>



    <img src={% static "12.png" %} style='top:800px; position:relative;  left:-150px; border:3px solid black;border-radius:10px;'>


      
       <h4 style='color:blue;position:relative;top:1000px;'> designed and developed by balaji<h4>
      </center>
          </body>
      </html>

 
admin.html

      {% load static %}
      
      <html>
          <head>
              <style>
      
                  body{
                      background:linear-gradient(300deg,white,pink)
                  }
                  .head{
                      color:black;
                      text-shadow: 4px 4px 4px white;
                      position:relative;
                      top:35px;
                  }
                  .title{
                      color:black;
                      text-shadow: 4px 4px 4px white;
                      position:aboslute;
                      top:35px;
                  }
                  button{
                      position:relative;
                      top:40px;
                      width:200px;
                      height:50px;
                      color:white;
                      background:black;
                  }
                  img{
                      height:100x;
                      width:100px;
                      position:relative;
                      left:450px;
                      top:-65px;
      
                      
                  }
              </style>
      
      
      
          </head>
          <body>
              <div class="head">
                  <center><h1>Smoke Flying Chai Shop</h1></div></center>
                  <img src={% static "chai.png" %} >
      <div class="title">
                   <center>   <h1>Administration</h1></center></div>
      
                 <center> 
                  <a href='/'><button>Home</button></a>
      
                  <a href='/menu'><button>Menu</button></a>
                 <a href='/admin'> <button>Administration</button></a>
                 <a href='/contact'> <button>Contact Us</button></a>
      <center>
      <img src={% static "enish.png" %} style='top:100px; position:relative;  left:100px;height:200px;width:240px; border:3px solid black;border-radius:10px;'>
      
       <img src={% static "Ae.png" %} style='top:100px; position:relative; height:200px;width:240px; left:300px; border:3px solid black;border-radius:10px;' >
          
          
          <img src={% static "balaji.png" %} style='top:100px; position:relative;  left:500px; height:200px;width:240px;border:3px solid black;border-radius:10px;'>
       
      <img src={% static "nigga.png" %} style='top:400px; position:relative;  left:-650px;height:200px;width:240px; border:3px solid black;border-radius:10px;'>
      
      <img src={% static "priyan.png" %} style='top:400px; position:relative;  left:-460px;height:200px;width:240px; border:3px solid black;border-radius:10px;'>
      
      <img src={% static "rosh.png" %} style='top:400px; position:relative; height:200px;width:240px; left:-250px; border:3px solid black;border-radius:10px;' >
      </center>
      
         <h4 style='color:blue;position:relative;top:600px;'> designed and developed by balaji<h4>
      </center>
          </body>
      </html>
 contact.html
     
     {% load static %}

        <html>
            <head>
                <style>

                    body{
                        background:linear-gradient(300deg,white,pink)
                    }
                    .head{
                        color:black;
                        text-shadow: 4px 4px 4px white;
                        position:relative;
                        top:35px;
                    }
                    .title{
                        color:black;
                        text-shadow: 4px 4px 4px white;
                        position:aboslute;
                        top:35px;
                    }
                    button{
                        position:relative;
                        top:40px;
                        width:200px;
                        height:50px;
                        color:white;
                        background:black;
                    }
                    img{
                        height:100x;
                        width:100px;
                        position:relative;
                        left:450px;
                        top:-65px;

                        
                    }
                </style>



                    </head>
                    <body>
                        <div class="head">
                            <center><h1>Smoke Flying Chai Shop</h1></div></center>
                            <img src={% static "chai.png" %} >
                <div class="title">
                    <center>   <h1>Contact Us</h1></center></div>

                        <center> 
                            <a href='/'><button>Home</button></a>

                            <a href='/menu'><button>Menu</button></a>
                        <a href='/admin'> <button>Administration</button></a>
                        <a href='/contact'> <button>Contact Us</button></a>


        <div style="max-width: 600px;position:relative;top:200px; margin: auto; background: linear-gradient(300deg,pink,white); padding: 20px; border-radius: 8px; box-shadow: 0px 2px 5px rgba(0,0,0,0.2);"> 

            
            <h2 style="text-align: center; color: #181818ff;">Contact Us</h2> 
            <p style="text-align: center; font-size: 14px; color: #070707ff;"> We'd love to hear from you! Get in touch using the details below. </p>
            <div style="margin-top: 20px; line-height: 1.8; color: #0c0c0cff; font-size: 15px;"> <p><strong>📍 Address:</strong>Street, Chennai, India</p> 
                <p><strong>📞 Phone:</strong> 
                    +91 98765 43210</p>
                    <p><strong>✉️ Email:</strong>
                        sangeethathandapani7@gmail.com</p> 
                        </div>
                        <div style="margin-top: 20px; text-align: center;"> 
                            <a href="mailto:sangeethathandapani7@gmail.com" style="text-decoration: none; background: #011121ff; color: white; padding: 10px 20px; border-radius: 5px; font-size: 14px;"> Send Email </a> 
                        </div>
                    </div>
        <h4 style='color:blue;position:relative;top:600px;'> designed and developed by balaji<h4>
        </center>
            </body>
        </html>



# OUTPUT:
<img width="1920" height="1080" alt="Screenshot 2025-10-04 205346" src="https://github.com/user-attachments/assets/91f84223-d37d-483a-93fb-df0e98a23e8d" />
<img width="1920" height="1080" alt="Screenshot 2025-10-04 205454" src="https://github.com/user-attachments/assets/abb1a3ab-ce0d-443d-9f02-25e3ae211f27" />
<img width="1920" height="1080" alt="Screenshot 2025-10-04 205513" src="https://github.com/user-attachments/assets/8e482c11-6425-4ce7-94c2-f5526e316b54" />
<img width="1920" height="1080" alt="Screenshot 2025-10-04 205528" src="https://github.com/user-attachments/assets/3f43e4aa-2f07-4a2c-b059-6930700d5ef1" />
<img width="1920" height="1080" alt="Screenshot 2025-10-04 205542" src="https://github.com/user-attachments/assets/50c45096-82e7-43a6-b4fc-0842ca94fda6" />



# RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
