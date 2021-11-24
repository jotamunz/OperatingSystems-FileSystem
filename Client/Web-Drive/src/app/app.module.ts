import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material/material.module';

import { AuthenticationGuard } from './Guards/authentication.guard';

import { AppComponent } from './app.component';
import { LoginComponent } from './Components/login/login.component';
import { SignUpComponent } from './Components/sign-up/sign-up.component';
import { DriveComponent } from './Components/drive/drive.component';
import { FileViewComponent } from './Components/file-view/file-view.component';
import { CreateDirectoryComponent } from './Components/create-directory/create-directory.component';

@NgModule({
  declarations: [AppComponent, LoginComponent, SignUpComponent, DriveComponent, FileViewComponent, CreateDirectoryComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule,
  ],
  providers: [AuthenticationGuard],
  bootstrap: [AppComponent],
})
export class AppModule {}
