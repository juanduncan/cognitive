/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_AVIO505_THREE_CH_MUX_RTDEX_V2_H
#define INCLUDED_AVIO505_THREE_CH_MUX_RTDEX_V2_H

#include <avio505/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace avio505 {

    /*!
     * \brief <+description of block+>
     * \ingroup avio505
     *
     */
    class AVIO505_API three_ch_mux_rtdex_v2 : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<three_ch_mux_rtdex_v2> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of avio505::three_ch_mux_rtdex_v2.
       *
       * To avoid accidental use of raw pointers, avio505::three_ch_mux_rtdex_v2's
       * constructor is in a private implementation
       * class. avio505::three_ch_mux_rtdex_v2::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace avio505
} // namespace gr

#endif /* INCLUDED_AVIO505_THREE_CH_MUX_RTDEX_V2_H */

