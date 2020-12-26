var course
$('option').click(function(){
course=$(this).text();
console.log(course)
})
$('.SSR').click(function(){
    if(course=='B.P.T' && $(this).text()=='Highlights')
    {

        $('p').text('B.P.T Highlights '+courses);
    }
    else if(course=='B.M.L.T' && $(this).text()=='Highlights')
    {
        $('p').text('B.M.L.T Highlights');
    }
    else if(course=='D.M.L.T' && $(this).text()=='Highlights')
    {
        $('p').text('D.M.L.T Highlights');
    }
    else if(course=='C.C.H' && $(this).text()=='Highlights')
    {
        $('p').text('C.C.H Highlights');
    }
    else if(course=='M.M.L.T' && $(this).text()=='Highlights')
    {
        $('p').text('M.M.L.T Highlights');
    }
    
})
src='{% static "courses.js" %}'


class Category(models.Model):
    cat=models.CharField('Category',max_length=50,default='')
    image=models.ImageField('Image',upload_to="Category/Images",default='')
    def __str__(self):
        return self.cat


        class Infrasturcture(models.Model):
        image=models.ImageField('Image',upload_to='Infrastructure/images',default='')
        title=models.CharField('Title',max_length=100,default='')
        description=models.CharField('Description',max_length=500,default='')
        def __str__(self):
            return self.title
            admin.site.register(Infrasturcture)