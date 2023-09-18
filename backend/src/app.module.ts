import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ConfigModule } from '@nestjs/config'
import { AuthService } from './auth/auth.service';
import { AuthController } from './auth/auth.controller';

@Module({
  imports: [ConfigModule.forRoot({
    envFilePath: '.env.backend',
    isGlobal: true,
  })],
  controllers: [AppController, AuthController],
  providers: [AppService, AuthService],
})
export class AppModule {}
