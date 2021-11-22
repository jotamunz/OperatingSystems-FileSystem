import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from './Components/login/login.component';
import { DriveComponent } from './Components/drive/drive.component';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'my-drive', component: DriveComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
