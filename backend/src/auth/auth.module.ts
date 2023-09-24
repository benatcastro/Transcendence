import { Module } from "@nestjs/common";
import { UserModule } from "src/user/user.module";
import { AuthController } from "./auth.controller";
import { UserService } from "src/user/user.service";
import { AuthService } from "./auth.service";
import { HttpModule, HttpService } from "@nestjs/axios";
import { PrismaService } from "src/prisma/prisma.service";

@Module({
  imports: [UserModule, HttpModule],
  controllers: [AuthController],
  providers: [
    AuthService,
    UserService,
    PrismaService,
  ],
})
export class AuthModule {}
