import { NgModule } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatCardModule } from '@angular/material/card';
import { MatMenuModule } from '@angular/material/menu';
import { MatListModule } from '@angular/material/list'


const MaterialComponents = [
  MatButtonModule,
  MatInputModule,
  FormsModule,
  MatIconModule,
  MatSnackBarModule,
  ReactiveFormsModule,
  MatDialogModule,
  MatProgressBarModule,
  MatCardModule,
  MatMenuModule,
  MatListModule,
];

@NgModule({
  imports: [MaterialComponents],
  exports: [MaterialComponents],
  providers: [{ provide: MatDialogRef, useValue: {} }],
})
export class MaterialModule {}
