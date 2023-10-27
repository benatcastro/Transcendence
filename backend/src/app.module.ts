import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PrismaService } from './prisma/prisma.service';
import { UserModule } from './user/user.module';
import { AuthModule } from './auth/auth.module';
import { ThrottlerModule } from '@nestjs/throttler';

@Module({
  imports: [UserModule, AuthModule, ThrottlerModule.forRoot([{
    ttl: 6000,
    limit: 10
    ,
  }])], // Combinar todas las importaciones en una sola declaración
  controllers: [AppController],
  providers: [AppService, PrismaService],
})
export class AppModule {}
