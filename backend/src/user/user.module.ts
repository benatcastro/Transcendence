import { Global, Module } from '@nestjs/common';
import { UserController } from './user.controller';
import { PrismaService } from 'src/prisma/prisma.service';
import { UserService } from './user.service';

@Global()
@Module({
    imports: [],
    controllers: [UserController],
    providers: [PrismaService, UserService],
    exports: [UserService]
})
export class UserModule {}
