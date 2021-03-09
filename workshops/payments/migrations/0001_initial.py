# ----------------------------------------------------------------------------
# Copyright (c) 2017-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# Generated by Django 2.1.7 on 2019-02-28 19:01

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('contact_name', models.CharField(max_length=300)),
                ('contact_email', models.EmailField(max_length=254)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='order total (USD)')),
                ('order_datetime', models.DateTimeField(auto_now_add=True)),
                ('billed_total', models.CharField(blank=True, help_text='This is the confirmed paid amount from NAU', max_length=300, verbose_name='billed total (USD)')),
                ('billed_datetime', models.CharField(blank=True, help_text='This is the confirmed date and time of payment', max_length=300, verbose_name='billed date & time')),
                ('refunded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=500)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Order')),
            ],
        ),
        migrations.CreateModel(
            name='PosterOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('sort_order', models.IntegerField(help_text='This value is used to sort the display order of the poster presentation options')),
            ],
            options={
                'ordering': ('sort_order',),
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price (USD)')),
                ('capacity', models.PositiveIntegerField()),
                ('private', models.BooleanField(default=False)),
                ('discount_code', models.SlugField(blank=True, help_text='This will be the code given to a customer receiving a discount in the form of https://workshops.qiime2.org/workshop_slug/rate=discount_code')),
                ('sales_open', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('dedicated_qiime2', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=300)),
                ('description', markdownx.models.MarkdownxField()),
                ('email_description', markdownx.models.MarkdownxField(blank=True, help_text='This is the text that is emailed to all workshop attendees when their payment is processed. Supports Markdown.')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('url', models.URLField(blank=True, max_length=2000, verbose_name='URL')),
                ('slug', models.SlugField(help_text='This is the unique identifier for the URL (i.e. title-YYYY-MM-DD)')),
                ('draft', models.BooleanField(default=True, help_text='Draft workshops do not show up on the workshop list overview')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='workshop',
            unique_together={('title', 'slug')},
        ),
        migrations.AddField(
            model_name='rate',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Workshop'),
        ),
        migrations.AddField(
            model_name='posteroption',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Workshop'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.PosterOption'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Rate'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='workshops',
            field=models.ManyToManyField(blank=True, related_name='instructors', to='payments.Workshop'),
        ),
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('order', 'rate', 'email')},
        ),
    ]
