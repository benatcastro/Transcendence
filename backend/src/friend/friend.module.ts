import { Module } from '@nestjs/common';
import { FriendController } from './friend.controller';
import { FriendService } from './friend.service';
import { PrismaService } from 'src/prisma/prisma.service';

@Module({
  controllers: [FriendController],
  providers: [PrismaService, FriendService]
})
export class FriendModule {}
