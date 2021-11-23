import { NgModule } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatDialogModule, MatDialogRef } from '@angular/material/dialog';

const MaterialComponents = [
  MatButtonModule,
  MatInputModule,
  FormsModule,
  MatIconModule,
  MatSnackBarModule,
  ReactiveFormsModule,
  MatDialogModule,
];

@NgModule({
  imports: [MaterialComponents],
  exports: [MaterialComponents],
  providers: [{ provide: MatDialogRef, useValue: {} }],
})
export class MaterialModule {}
