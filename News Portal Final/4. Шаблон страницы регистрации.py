html
<h2>Регистрация</h2>  
<form method="POST">  
  {% csrf_token %}  
  {{ form.as_p }}  
  <button type="submit">Зарегистрироваться</button>  
</form>  