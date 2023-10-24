import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { AuthController } from './auth.controller';
import { UserModule } from 'src/user/user.module';
import { HttpModule } from '@nestjs/axios';
@Module({
  imports: [HttpModule, UserModule],    
  providers: [AuthService],
  controllers: [AuthController]
})
export class AuthModule {}
