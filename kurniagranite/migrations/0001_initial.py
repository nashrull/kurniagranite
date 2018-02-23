# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-31 04:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namakategori', models.CharField(max_length=32)),
                ('is_active', models.CharField(choices=[('0', 'Tidak Aktif'), ('1', 'Aktif'), ('2', 'Hapus')], default='1', max_length=3)),
                ('slug', models.CharField(max_length=32)),
                ('created_by', models.CharField(max_length=32, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['namakategori'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namamaterial', models.CharField(max_length=32)),
                ('slug', models.SlugField(unique=True)),
                ('deskripsi', models.TextField(blank=True, default='tidak ada keterangan tentang produk ini')),
                ('metafield', models.TextField(blank=True)),
                ('gambar1', models.ImageField(blank=True, default='media/noimage.png', upload_to='gambar/material/%Y/%m')),
                ('gambar2', models.ImageField(blank=True, default='media/noimage.png', upload_to='gambar/material/%Y/%m')),
                ('gambar3', models.ImageField(blank=True, default='media/noimage.png', upload_to='gambar/material/%Y/%m')),
                ('gambar4', models.ImageField(blank=True, default='media/noimage.png', upload_to='gambar/material/%Y/%m')),
                ('gambar5', models.ImageField(blank=True, default='media/noimage.png', upload_to='gambar/material/%Y/%m')),
                ('is_active', models.CharField(choices=[('0', 'Tidak Aktif'), ('1', 'Aktif'), ('2', 'Hapus')], default='1', max_length=3)),
                ('created_by', models.CharField(max_length=32, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_hp', models.CharField(default='Belum Diisi', max_length=16)),
                ('nama_user', models.CharField(default='Belum Diisi', max_length=32)),
                ('poto', models.ImageField(blank=True, default='media/noimage.png', upload_to='user/potoprofile/%Y/%m')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('id_login', models.ForeignKey(default='Nope', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaproduct', models.CharField(max_length=32)),
                ('deskripsi', models.TextField(blank=True, default='tidak ada keterangan tentang produk ini')),
                ('gambar1', models.FileField(blank=True, upload_to='gambar/product/%Y/%m')),
                ('gambar2', models.FileField(blank=True, upload_to='gambar/product/%Y/%m')),
                ('gambar3', models.FileField(blank=True, upload_to='gambar/product/%Y/%m')),
                ('gambar4', models.FileField(blank=True, upload_to='gambar/product/%Y/%m')),
                ('gambar5', models.FileField(blank=True, upload_to='gambar/product/%Y/%m')),
                ('is_active', models.CharField(choices=[('0', 'Tidak Aktif'), ('1', 'Aktif'), ('2', 'Hapus')], default='1', max_length=3)),
                ('created_by', models.CharField(max_length=32, null=True)),
                ('harga', models.CharField(default='0', max_length=32)),
                ('show_harga', models.CharField(choices=[('0', 'Tidak Ditampilkan'), ('1', 'Tampilkan')], default='2', max_length=1)),
                ('slug', models.SlugField(default='d')),
                ('metafield', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurniagranite.Kategori')),
                ('material', models.ManyToManyField(to='kurniagranite.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(blank=True, max_length=32)),
                ('slug', models.CharField(blank=True, max_length=64)),
                ('link', models.CharField(blank=True, max_length=64, null=True)),
                ('gambar', models.FileField(blank=True, upload_to='gambar/slider/%Y/%m')),
                ('is_active', models.CharField(choices=[('0', 'Tidak Aktif'), ('1', 'Aktif'), ('2', 'Hapus')], default='1', max_length=3)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]